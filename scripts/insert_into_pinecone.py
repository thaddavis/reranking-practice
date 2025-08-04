#!/usr/bin/env python3
"""
Script to chunk markdown files and insert them into a Pinecone index with embeddings.

This script:
1. Processes all markdown files in the raw_data folder using the markdown_processor module
2. Generates embeddings for each chunk using OpenAI's Ada 002 model
3. Inserts the embedded chunks into a Pinecone index with metadata

Usage:
    python scripts/insert_into_pinecone.py

Environment Variables Required:
    PINECONE_API_KEY - Your Pinecone API key
    PINECONE_INDEX_NAME - Name of the Pinecone index
    OPENAI_API_KEY - Your OpenAI API key for generating embeddings
"""

import os
import sys
import time
import hashlib
from pathlib import Path
from typing import List, Dict, Any
from pinecone import Pinecone
import openai
from dotenv import load_dotenv

# Import the markdown processor module
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from markdown_processor import (
    setup_text_splitter,
    process_multiple_markdown_files,
    get_processing_stats
)


def load_environment():
    """Load environment variables from .env file."""
    # Load from .env file in project root
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print(f"Loaded environment from {env_file}")
    else:
        print("No .env file found, using system environment variables")


def get_required_env_vars():
    """Get required environment variables with validation."""
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    missing_vars = []
    if not pinecone_api_key:
        missing_vars.append("PINECONE_API_KEY")
    if not index_name:
        missing_vars.append("PINECONE_INDEX_NAME")
    if not openai_api_key:
        missing_vars.append("OPENAI_API_KEY")
    
    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these in your .env file or environment.")
        print("Example .env file:")
        print("PINECONE_API_KEY=your-pinecone-api-key")
        print("PINECONE_INDEX_NAME=your-index-name")
        print("OPENAI_API_KEY=your-openai-api-key")
        sys.exit(1)
    
    return pinecone_api_key, index_name, openai_api_key


def generate_embeddings(
    texts: List[str], 
    openai_api_key: str, 
    model: str = "text-embedding-ada-002",
    batch_size: int = 50,
    delay_between_batches: float = 1.0
) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using OpenAI's API with batching and rate limiting.
    
    Args:
        texts (List[str]): List of text chunks to embed
        openai_api_key (str): OpenAI API key
        model (str): Embedding model to use
        batch_size (int): Number of texts to process per batch
        delay_between_batches (float): Delay in seconds between batches
        
    Returns:
        List[List[float]]: List of embedding vectors
    """
    try:
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=openai_api_key)
        
        print(f"Generating embeddings for {len(texts)} chunks using {model}...")
        print(f"Processing in batches of {batch_size} with {delay_between_batches}s delay between batches")
        
        all_embeddings = []
        
        # Process in batches to handle rate limits
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_num = i // batch_size + 1
            total_batches = (len(texts) + batch_size - 1) // batch_size
            
            print(f"Processing batch {batch_num}/{total_batches} ({len(batch)} chunks)...")
            
            try:
                # Generate embeddings for this batch
                response = client.embeddings.create(
                    input=batch,
                    model=model
                )
                
                # Extract embedding vectors
                batch_embeddings = [item.embedding for item in response.data]
                all_embeddings.extend(batch_embeddings)
                
                print(f"✅ Batch {batch_num} completed ({len(batch_embeddings)} embeddings)")
                
                # Add delay between batches (except for the last one)
                if i + batch_size < len(texts):
                    time.sleep(delay_between_batches)
                    
            except openai.RateLimitError as e:
                print(f"⚠️  Rate limit hit on batch {batch_num}. Error: {e}")
                print("Suggestions:")
                print("1. Check your OpenAI API quota at https://platform.openai.com/usage")
                print(f"2. Try reducing batch_size (current: {batch_size})")
                print(f"3. Increase delay_between_batches (current: {delay_between_batches}s)")
                print("4. Consider using a free alternative embedding model")
                raise
                
            except Exception as e:
                print(f"❌ Error in batch {batch_num}: {e}")
                raise
        
        print(f"✅ Generated {len(all_embeddings)} total embeddings")
        return all_embeddings
        
    except openai.RateLimitError as e:
        print(f"\n❌ OpenAI API Quota Exceeded!")
        print(f"Error: {e}")
        print("\n🔧 Solutions:")
        print("1. Check your OpenAI billing and usage: https://platform.openai.com/usage")
        print("2. Add credits to your OpenAI account")
        print("3. Wait for your quota to reset (if on free tier)")
        print("4. Use a free local embedding model instead")
        print("\n💡 Alternative: Run with --use-local-embeddings flag (coming soon)")
        raise
        
    except Exception as e:
        print(f"❌ Error generating embeddings: {e}")
        raise


def create_vector_id(file_name: str, chunk_index: int) -> str:
    """
    Create a unique vector ID for a chunk.
    
    Args:
        file_name (str): Name of the source file
        chunk_index (int): Index of the chunk within the file
        
    Returns:
        str: Unique vector ID
    """
    # Create a deterministic ID based on file name and chunk index
    id_string = f"{file_name}_{chunk_index}"
    # Use hash to ensure consistent length and avoid special characters
    return hashlib.md5(id_string.encode()).hexdigest()


def prepare_vectors_for_pinecone(processed_files: List[Dict[str, Any]], embeddings: List[List[float]]) -> List[Dict]:
    """
    Prepare vectors with metadata for Pinecone insertion.
    
    Args:
        processed_files (List[Dict]): Processed markdown file data
        embeddings (List[List[float]]): Corresponding embeddings
        
    Returns:
        List[Dict]: Vectors formatted for Pinecone
    """
    vectors = []
    embedding_index = 0
    
    for file_data in processed_files:
        if 'error' in file_data:
            continue
            
        file_name = file_data['file_name']
        front_matter = file_data['front_matter']
        chunks = file_data['chunks']
        
        for chunk_index, chunk_text in enumerate(chunks):
            if embedding_index >= len(embeddings):
                print(f"⚠️  Warning: Not enough embeddings for all chunks")
                break
                
            vector_id = create_vector_id(file_name, chunk_index)
            
            # Prepare metadata
            metadata = {
                'file_name': file_name,
                'chunk_index': chunk_index,
                'chunk_text': chunk_text,
                'chunk_length': len(chunk_text),
                'video_title': front_matter.get('video_title', ''),
                'video_url': front_matter.get('video_url', ''),
                'total_chunks_in_file': len(chunks)
            }
            
            vector = {
                'id': vector_id,
                'values': embeddings[embedding_index],
                'metadata': metadata
            }
            
            vectors.append(vector)
            embedding_index += 1
    
    return vectors


def insert_vectors_to_pinecone(vectors: List[Dict], pinecone_api_key: str, index_name: str, batch_size: int = 100):
    """
    Insert vectors into Pinecone index in batches.
    
    Args:
        vectors (List[Dict]): Vectors to insert
        pinecone_api_key (str): Pinecone API key
        index_name (str): Name of the Pinecone index
        batch_size (int): Number of vectors to insert per batch
    """
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=pinecone_api_key)
        index = pc.Index(index_name)
        
        print(f"Inserting {len(vectors)} vectors into Pinecone index '{index_name}'...")
        
        # Insert vectors in batches
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i + batch_size]
            
            print(f"Inserting batch {i//batch_size + 1}/{(len(vectors) + batch_size - 1)//batch_size} ({len(batch)} vectors)...")
            
            index.upsert(vectors=batch)
            
            # Small delay to avoid rate limiting
            if i + batch_size < len(vectors):
                time.sleep(1)
        
        print("✅ All vectors inserted successfully!")
        
        # Verify insertion
        print("\n🔍 Verifying insertion...")
        time.sleep(2)  # Wait for indexing
        stats = index.describe_index_stats()
        total_vectors = stats.get('total_vector_count', 0)
        print(f"Index now contains {total_vectors:,} vectors")
        
    except Exception as e:
        print(f"❌ Error inserting vectors into Pinecone: {e}")
        raise


def main():
    """Main function to process markdown files and insert into Pinecone."""
    print("Markdown to Pinecone Insertion Script")
    print("=" * 50)
    
    # Load environment variables
    load_environment()
    
    # Get required environment variables
    pinecone_api_key, index_name, openai_api_key = get_required_env_vars()
    
    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    raw_data_dir = project_root / "raw_data"
    
    if not raw_data_dir.exists():
        print(f"❌ Error: raw_data directory not found at {raw_data_dir}")
        sys.exit(1)
    
    # Step 1: Process markdown files
    print("\n📄 Step 1: Processing markdown files...")
    text_splitter = setup_text_splitter(
        chunk_size=1000,
        chunk_overlap=200,
        encoding_name="cl100k_base"
    )
    
    processed_files = process_multiple_markdown_files(
        directory_path=raw_data_dir,
        text_splitter=text_splitter,
        include_chunk_previews=False  # Don't need previews for embedding
    )
    
    if not processed_files:
        print("❌ No markdown files found to process")
        sys.exit(1)
    
    # Get processing stats
    stats = get_processing_stats(processed_files)
    print(f"✅ Processed {stats['successful_files']} files, created {stats['total_chunks']} chunks")
    
    # Step 2: Collect all chunks for embedding
    print("\n🔍 Step 2: Collecting chunks for embedding...")
    all_chunks = []
    for file_data in processed_files:
        if 'error' not in file_data:
            all_chunks.extend(file_data['chunks'])
    
    print(f"Found {len(all_chunks)} chunks total")
    
    # Step 3: Generate embeddings
    print(f"\n🤖 Step 3: Generating embeddings...")
    try:
        embeddings = generate_embeddings(
            all_chunks, 
            openai_api_key,
            batch_size=25,  # Smaller batches to be gentler on API limits
            delay_between_batches=2.0  # 2 second delay between batches
        )
    except Exception as e:
        print(f"\n❌ Failed to generate embeddings. Exiting...")
        print(f"\n💡 Quick fixes:")
        print("1. Check OpenAI account quota: https://platform.openai.com/usage")
        print("2. Reduce the number of files in raw_data folder")
        print("3. Use smaller chunk sizes in markdown_processor")
        sys.exit(1)
    
    # Step 4: Prepare vectors for Pinecone
    print(f"\n📦 Step 4: Preparing vectors for Pinecone...")
    vectors = prepare_vectors_for_pinecone(processed_files, embeddings)
    print(f"Prepared {len(vectors)} vectors with metadata")
    
    # Step 5: Insert into Pinecone
    print(f"\n🚀 Step 5: Inserting vectors into Pinecone...")
    insert_vectors_to_pinecone(vectors, pinecone_api_key, index_name)
    
    print("\n✅ Pipeline completed successfully!")
    print(f"   - Processed: {stats['successful_files']} files")
    print(f"   - Created: {len(vectors)} embedded chunks")
    print(f"   - Inserted into: {index_name}")


if __name__ == "__main__":
    main()