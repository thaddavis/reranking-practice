#!/usr/bin/env python3
"""
Script to perform similarity search against a Pinecone index with Cohere re-ranking.

This script:
1. Takes a query text as input
2. Generates embeddings for the query using OpenAI's Ada 002 model
3. Performs initial similarity search against the Pinecone index
4. Re-ranks the results using Cohere's re-ranking model for improved relevance
5. Returns the re-ranked results with both similarity and relevance scores

Usage:
    python scripts/search_with_reranking.py "your search query here"
    python scripts/search_with_reranking.py --interactive
    uv run scripts/search_with_reranking.py --query "machine learning" --initial-top-k 10 --rerank-top-k 5

Environment Variables Required:
    PINECONE_API_KEY - Your Pinecone API key
    PINECONE_INDEX_NAME - Name of the Pinecone index
    OPENAI_API_KEY - Your OpenAI API key for generating embeddings
    COHERE_API_KEY - Your Cohere API key for re-ranking
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple
from pinecone import Pinecone
import openai
import cohere
from dotenv import load_dotenv


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
    cohere_api_key = os.getenv("COHERE_API_KEY")
    
    missing_vars = []
    if not pinecone_api_key:
        missing_vars.append("PINECONE_API_KEY")
    if not index_name:
        missing_vars.append("PINECONE_INDEX_NAME")
    if not openai_api_key:
        missing_vars.append("OPENAI_API_KEY")
    if not cohere_api_key:
        missing_vars.append("COHERE_API_KEY")
    
    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these in your .env file or environment.")
        print("Example .env file:")
        print("PINECONE_API_KEY=your-pinecone-api-key")
        print("PINECONE_INDEX_NAME=your-index-name")
        print("OPENAI_API_KEY=your-openai-api-key")
        print("COHERE_API_KEY=your-cohere-api-key")
        sys.exit(1)
    
    return pinecone_api_key, index_name, openai_api_key, cohere_api_key


def generate_query_embedding(query: str, openai_api_key: str, model: str = "text-embedding-ada-002") -> List[float]:
    """
    Generate embedding for a search query.
    
    Args:
        query (str): Search query text
        openai_api_key (str): OpenAI API key
        model (str): Embedding model to use
        
    Returns:
        List[float]: Query embedding vector
    """
    try:
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=openai_api_key)
        
        print(f"Generating embedding for query: '{query[:50]}{'...' if len(query) > 50 else ''}'")
        
        # Generate embedding
        response = client.embeddings.create(
            input=[query],
            model=model
        )
        
        # Extract embedding vector
        embedding = response.data[0].embedding
        
        print(f"✅ Generated query embedding ({len(embedding)} dimensions)")
        return embedding
        
    except openai.RateLimitError as e:
        print(f"❌ OpenAI API Quota Exceeded!")
        print(f"Error: {e}")
        print("\n🔧 Solutions:")
        print("1. Check your OpenAI billing and usage: https://platform.openai.com/usage")
        print("2. Add credits to your OpenAI account")
        raise
        
    except Exception as e:
        print(f"❌ Error generating query embedding: {e}")
        raise


def search_pinecone_index(
    query_embedding: List[float],
    pinecone_api_key: str,
    index_name: str,
    top_k: int = 20,  # Get more candidates for re-ranking
    include_metadata: bool = True
) -> Dict[str, Any]:
    """
    Search Pinecone index for similar vectors.
    
    Args:
        query_embedding (List[float]): Query embedding vector
        pinecone_api_key (str): Pinecone API key
        index_name (str): Name of the Pinecone index
        top_k (int): Number of similar results to return
        include_metadata (bool): Whether to include metadata in results
        
    Returns:
        Dict[str, Any]: Search results from Pinecone
    """
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=pinecone_api_key)
        index = pc.Index(index_name)
        
        print(f"Searching index '{index_name}' for {top_k} initial candidates...")
        
        # Perform similarity search
        results = index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=include_metadata
        )
        
        print(f"✅ Found {len(results.get('matches', []))} initial candidates")
        return results
        
    except Exception as e:
        print(f"❌ Error searching Pinecone index: {e}")
        raise


def rerank_with_cohere(
    query: str,
    documents: List[Dict[str, Any]],
    cohere_api_key: str,
    model: str = "rerank-v3.5",
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    Re-rank documents using Cohere's re-ranking model.
    
    Args:
        query (str): Original search query
        documents (List[Dict]): Documents from Pinecone search with metadata
        cohere_api_key (str): Cohere API key
        model (str): Cohere re-ranking model to use
        top_k (int): Number of top results to return after re-ranking
        
    Returns:
        List[Dict]: Re-ranked documents with relevance scores
    """
    try:
        # Initialize Cohere client
        co = cohere.Client(api_key=cohere_api_key)
        
        print(f"Re-ranking {len(documents)} documents using Cohere {model}...")
        
        # Prepare documents for re-ranking (extract text content)
        doc_texts = []
        for doc in documents:
            metadata = doc.get('metadata', {})
            chunk_text = metadata.get('chunk_text', '')
            
            # If no chunk text, create a summary from available metadata
            if not chunk_text:
                video_title = metadata.get('video_title', '')
                file_name = metadata.get('file_name', '')
                chunk_text = f"{video_title} {file_name}".strip()
            
            doc_texts.append(chunk_text)
        
        # Perform re-ranking
        rerank_response = co.rerank(
            query=query,
            documents=doc_texts,
            model=model,
            top_n=top_k,
            return_documents=True
        )
        
        # Combine re-ranking results with original metadata
        reranked_docs = []
        for result in rerank_response.results:
            original_doc = documents[result.index]
            reranked_doc = {
                'original_similarity_score': original_doc.get('score', 0),
                'rerank_relevance_score': result.relevance_score,
                'rerank_index': result.index,
                'metadata': original_doc.get('metadata', {}),
                'id': original_doc.get('id', ''),
                'document_text': result.document.text if hasattr(result.document, 'text') else doc_texts[result.index]
            }
            reranked_docs.append(reranked_doc)
        
        print(f"✅ Re-ranked to top {len(reranked_docs)} most relevant results")
        return reranked_docs
        
    except Exception as e:
        print(f"❌ Error re-ranking with Cohere: {e}")
        print("💡 Make sure you have a valid Cohere API key and sufficient credits")
        raise


def format_reranked_results(results: List[Dict[str, Any]], show_full_text: bool = False) -> None:
    """
    Format and display re-ranked search results in a readable way.
    
    Args:
        results (List[Dict]): Re-ranked results with both similarity and relevance scores
        show_full_text (bool): Whether to show full chunk text or just preview
    """
    if not results:
        print("No similar chunks found.")
        return
    
    print(f"\n🔍 Re-ranked Search Results ({len(results)} matches)")
    print("=" * 80)
    
    for i, result in enumerate(results, 1):
        similarity_score = result.get('original_similarity_score', 0)
        relevance_score = result.get('rerank_relevance_score', 0)
        metadata = result.get('metadata', {})
        
        print(f"\n📄 Result {i}")
        print("-" * 50)
        print(f"Similarity Score: {similarity_score:.4f} | Relevance Score: {relevance_score:.4f}")
        
        # File and chunk info
        file_name = metadata.get('file_name', 'Unknown')
        chunk_index = metadata.get('chunk_index', 'Unknown')
        total_chunks = metadata.get('total_chunks_in_file', 'Unknown')
        print(f"File: {file_name}")
        print(f"Chunk: {chunk_index + 1}/{total_chunks}" if isinstance(chunk_index, int) else f"Chunk: {chunk_index}")
        
        # Video metadata
        video_title = metadata.get('video_title', '')
        video_url = metadata.get('video_url', '')
        if video_title:
            print(f"Video: {video_title}")
        if video_url:
            print(f"URL: {video_url}")
        
        # Chunk content
        chunk_text = metadata.get('chunk_text', '')
        chunk_length = metadata.get('chunk_length', len(chunk_text))
        print(f"Length: {chunk_length} characters")
        
        if chunk_text:
            if show_full_text or len(chunk_text) <= 200:
                print(f"\nContent:\n{chunk_text}")
            else:
                preview = chunk_text[:200] + "..."
                print(f"\nPreview:\n{preview}")
                print(f"\n[Use --full-text to see complete content]")
        
        if i < len(results):
            print("\n" + "─" * 50)


def interactive_search(pinecone_api_key: str, index_name: str, openai_api_key: str, cohere_api_key: str):
    """
    Interactive search mode where user can enter multiple queries.
    
    Args:
        pinecone_api_key (str): Pinecone API key
        index_name (str): Name of the Pinecone index
        openai_api_key (str): OpenAI API key
        cohere_api_key (str): Cohere API key
    """
    print("\n🔄 Interactive Re-ranking Search Mode")
    print("Enter your search queries (or 'quit' to exit)")
    print("=" * 50)
    
    while True:
        try:
            query = input("\n🔍 Enter search query: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not query:
                print("Please enter a search query.")
                continue
            
            # Get search parameters
            try:
                initial_k_input = input("Initial candidates to fetch (default 20): ").strip()
                initial_k = int(initial_k_input) if initial_k_input else 20
            except ValueError:
                initial_k = 20
                
            try:
                rerank_k_input = input("Final results after re-ranking (default 5): ").strip()
                rerank_k = int(rerank_k_input) if rerank_k_input else 5
            except ValueError:
                rerank_k = 5
                
            show_full = input("Show full text? (y/N): ").strip().lower() == 'y'
            
            # Perform search and re-ranking
            query_embedding = generate_query_embedding(query, openai_api_key)
            initial_results = search_pinecone_index(query_embedding, pinecone_api_key, index_name, initial_k)
            
            # Re-rank results
            candidates = initial_results.get('matches', [])
            if candidates:
                reranked_results = rerank_with_cohere(query, candidates, cohere_api_key, top_k=rerank_k)
                format_reranked_results(reranked_results, show_full_text=show_full)
            else:
                print("No candidates found for re-ranking.")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error during search: {e}")
            continue


def main():
    """Main function to handle command-line arguments and perform search with re-ranking."""
    parser = argparse.ArgumentParser(
        description="Search Pinecone index with Cohere re-ranking for improved relevance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/search_with_reranking.py "machine learning"
  python scripts/search_with_reranking.py --query "docker deployment" --initial-top-k 15 --rerank-top-k 3
  python scripts/search_with_reranking.py --interactive
  python scripts/search_with_reranking.py "OpenAI API" --full-text
        """
    )
    
    parser.add_argument(
        'query',
        nargs='?',
        help='Search query text'
    )
    
    parser.add_argument(
        '--query',
        dest='query_flag',
        type=str,
        help='Search query text (alternative to positional argument)'
    )
    
    parser.add_argument(
        '--initial-top-k',
        type=int,
        default=20,
        help='Number of initial candidates to fetch from Pinecone (default: 20)'
    )
    
    parser.add_argument(
        '--rerank-top-k',
        type=int,
        default=5,
        help='Number of final results to return after re-ranking (default: 5)'
    )
    
    parser.add_argument(
        '--full-text',
        action='store_true',
        help='Show full chunk text instead of preview'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Enter interactive search mode'
    )
    
    args = parser.parse_args()
    
    print("Pinecone Similarity Search with Cohere Re-ranking")
    print("=" * 55)
    
    # Load environment variables
    load_environment()
    
    # Get required environment variables
    pinecone_api_key, index_name, openai_api_key, cohere_api_key = get_required_env_vars()
    
    # Check if index exists and get stats
    try:
        pc = Pinecone(api_key=pinecone_api_key)
        index = pc.Index(index_name)
        stats = index.describe_index_stats()
        total_vectors = stats.get('total_vector_count', 0)
        print(f"Connected to index '{index_name}' with {total_vectors:,} vectors")
        
        if total_vectors == 0:
            print("⚠️  Warning: Index appears to be empty. Insert some data first.")
            return
            
    except Exception as e:
        print(f"❌ Error connecting to Pinecone index: {e}")
        return
    
    # Handle interactive mode
    if args.interactive:
        interactive_search(pinecone_api_key, index_name, openai_api_key, cohere_api_key)
        return
    
    # Get query from arguments (positional or flag)
    query = args.query or args.query_flag

    if not query:
        print("❌ Error: Please provide a search query")
        print("Use --help for usage examples")
        return
    
    try:
        # Generate query embedding
        query_embedding = generate_query_embedding(query, openai_api_key)
        
        # Initial similarity search
        initial_results = search_pinecone_index(
            query_embedding, 
            pinecone_api_key, 
            index_name, 
            top_k=args.initial_top_k
        )
        
        # Re-rank results with Cohere
        candidates = initial_results.get('matches', [])
        if candidates:
            reranked_results = rerank_with_cohere(
                query, 
                candidates, 
                cohere_api_key, 
                top_k=args.rerank_top_k
            )
            
            # Display results
            format_reranked_results(reranked_results, show_full_text=args.full_text)
        else:
            print("No candidates found for re-ranking.")
        
    except Exception as e:
        print(f"❌ Search failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()