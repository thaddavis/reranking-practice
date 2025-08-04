#!/usr/bin/env python3
"""
Test script to insert a small sample of markdown files into Pinecone.

This script processes only the 3 smallest files to test the pipeline 
without hitting OpenAI API quota limits.

Usage:
    python scripts/test_small_insert.py

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
sys.path.append(str(Path(__file__).parent))
from markdown_processor import (
    setup_text_splitter,
    process_markdown_file,
    get_processing_stats
)

from insert_into_pinecone import (
    load_environment,
    get_required_env_vars,
    generate_embeddings,
    prepare_vectors_for_pinecone,
    insert_vectors_to_pinecone
)


def get_smallest_files(directory_path: Path, max_files: int = 3) -> List[Path]:
    """
    Get the smallest markdown files for testing.
    
    Args:
        directory_path (Path): Directory containing markdown files
        max_files (int): Maximum number of files to return
        
    Returns:
        List[Path]: List of smallest markdown files
    """
    markdown_files = list(directory_path.glob("*.md"))
    
    # Sort by file size
    files_with_size = [(f, f.stat().st_size) for f in markdown_files]
    files_with_size.sort(key=lambda x: x[1])  # Sort by size
    
    # Return the smallest files
    smallest_files = [f for f, _ in files_with_size[:max_files]]
    
    print(f"Selected {len(smallest_files)} smallest files for testing:")
    for f, size in files_with_size[:max_files]:
        print(f"  - {f.name} ({size:,} bytes)")
    
    return smallest_files


def main():
    """Main function to test Pinecone insertion with small sample."""
    print("Test Pinecone Insertion Script (Small Sample)")
    print("=" * 60)
    
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
    
    # Step 1: Get smallest files for testing
    print("\n📄 Step 1: Selecting small sample files...")
    test_files = get_smallest_files(raw_data_dir, max_files=3)
    
    if not test_files:
        print("❌ No markdown files found")
        sys.exit(1)
    
    # Step 2: Process the test files
    print(f"\n📄 Step 2: Processing {len(test_files)} test files...")
    text_splitter = setup_text_splitter(
        chunk_size=800,  # Slightly smaller chunks for testing
        chunk_overlap=150,
        encoding_name="cl100k_base"
    )
    
    processed_files = []
    for file_path in test_files:
        result = process_markdown_file(file_path, text_splitter, include_chunk_previews=False)
        processed_files.append(result)
    
    # Get processing stats
    stats = get_processing_stats(processed_files)
    print(f"✅ Processed {stats['successful_files']} files, created {stats['total_chunks']} chunks")
    
    if stats['total_chunks'] == 0:
        print("❌ No chunks created from test files")
        sys.exit(1)
    
    # Step 3: Collect chunks
    print(f"\n🔍 Step 3: Collecting chunks from test files...")
    all_chunks = []
    for file_data in processed_files:
        if 'error' not in file_data:
            all_chunks.extend(file_data['chunks'])
    
    print(f"Found {len(all_chunks)} chunks total (much smaller for testing!)")
    
    # Step 4: Generate embeddings (with very conservative settings)
    print(f"\n🤖 Step 4: Generating embeddings...")
    try:
        embeddings = generate_embeddings(
            all_chunks, 
            openai_api_key,
            batch_size=10,  # Very small batches
            delay_between_batches=3.0  # Extra delay to be safe
        )
    except Exception as e:
        print(f"\n❌ Failed to generate embeddings even for small sample.")
        print(f"This likely means you need to add credits to your OpenAI account.")
        print(f"Error: {e}")
        sys.exit(1)
    
    # Step 5: Prepare vectors for Pinecone
    print(f"\n📦 Step 5: Preparing vectors for Pinecone...")
    vectors = prepare_vectors_for_pinecone(processed_files, embeddings)
    print(f"Prepared {len(vectors)} vectors with metadata")
    
    # Step 6: Insert into Pinecone
    print(f"\n🚀 Step 6: Inserting test vectors into Pinecone...")
    insert_vectors_to_pinecone(vectors, pinecone_api_key, index_name, batch_size=20)
    
    print("\n✅ Test pipeline completed successfully!")
    print(f"   - Processed: {stats['successful_files']} small files")
    print(f"   - Created: {len(vectors)} embedded chunks")
    print(f"   - Inserted into: {index_name}")
    print(f"\n💡 Next steps:")
    print(f"   1. Check your Pinecone index to verify the test data")
    print(f"   2. If successful, add OpenAI credits and run the full pipeline")
    print(f"   3. Use scripts/delete_pinecone_index.py to clear test data if needed")


if __name__ == "__main__":
    main()