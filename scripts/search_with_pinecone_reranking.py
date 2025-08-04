#!/usr/bin/env python3
"""
Script to perform similarity search with Pinecone's hosted reranking models.

This script demonstrates two approaches:
1. Integrated reranking: Reranking as part of the search query
2. Standalone reranking: Separate reranking operation after initial search

Available Pinecone-hosted reranking models:
- cohere-rerank-3.5: Cohere's leading reranking model
- bge-reranker-v2-m3: Multilingual reranking model  
- pinecone-rerank-v0: Pinecone's own state-of-the-art model

Usage:
    python scripts/search_with_pinecone_reranking.py "your search query here"
    python scripts/search_with_pinecone_reranking.py --query "machine learning" --model cohere-rerank-3.5
    python scripts/search_with_pinecone_reranking.py --interactive --method standalone

Environment Variables Required:
    PINECONE_API_KEY - Your Pinecone API key
    PINECONE_INDEX_NAME - Name of the Pinecone index
    OPENAI_API_KEY - Your OpenAI API key for generating embeddings
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any
from pinecone import Pinecone
import openai
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
        print("\n💡 Note: Only Pinecone API key needed for reranking (no separate Cohere key required)")
        sys.exit(1)
    
    return pinecone_api_key, index_name, openai_api_key


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


def search_with_integrated_reranking(
    query_text: str,
    pinecone_api_key: str,
    index_name: str,
    rerank_model: str = "cohere-rerank-3.5",
    initial_top_k: int = 20,
    rerank_top_n: int = 5
) -> Dict[str, Any]:
    """
    Search with integrated reranking using Pinecone's hosted reranking.
    
    Note: This method uses Pinecone's query API which handles embedding generation internally.
    
    Args:
        query_text (str): Original search query text
        pinecone_api_key (str): Pinecone API key
        index_name (str): Name of the Pinecone index
        rerank_model (str): Pinecone-hosted reranking model to use
        initial_top_k (int): Number of initial candidates to fetch
        rerank_top_n (int): Number of reranked results to return
        
    Returns:
        Dict[str, Any]: Search results with integrated reranking
    """
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=pinecone_api_key)
        index = pc.Index(index_name)
        
        print(f"🔄 Integrated reranking search using {rerank_model}...")
        print(f"Fetching {initial_top_k} candidates, reranking to top {rerank_top_n}")
        print("💡 Note: Using Pinecone's text query API (handles embedding generation internally)")
        
        # Perform search with integrated reranking using text query
        results = index.search(
            query={
                "inputs": {"text": query_text},
                "top_k": initial_top_k
            },
            rerank={
                "model": rerank_model,
                "top_n": rerank_top_n,
                "rank_fields": ["chunk_text"]
            },
            include_metadata=True
        )
        
        print(f"✅ Found {len(results.get('matches', []))} reranked results")
        return results
        
    except Exception as e:
        error_msg = str(e)
        if "PERMISSION_DENIED" in error_msg or "not authorized" in error_msg:
            print(f"❌ Error: Pinecone account not authorized for reranking models")
            print("💡 Solutions:")
            print("   1. Check your Pinecone plan - reranking may require paid tier")
            print("   2. Contact Pinecone support to enable reranking models")
            print("   3. Use the basic similarity search or direct Cohere reranking instead")
            print(f"   4. Try: python scripts/search_pinecone.py \"{query_text}\"")
        else:
            print(f"❌ Error in integrated reranking search: {e}")
            print("💡 Note: Integrated reranking requires Pinecone's query API with text input")
        raise


def search_with_standalone_reranking(
    query_text: str,
    query_embedding: List[float],
    pinecone_api_key: str,
    index_name: str,
    rerank_model: str = "cohere-rerank-3.5",
    initial_top_k: int = 20,
    rerank_top_n: int = 5
) -> Dict[str, Any]:
    """
    Search with standalone reranking using Pinecone's inference API.
    
    Args:
        query_text (str): Original search query text
        query_embedding (List[float]): Query embedding vector
        pinecone_api_key (str): Pinecone API key
        index_name (str): Name of the Pinecone index
        rerank_model (str): Pinecone-hosted reranking model to use
        initial_top_k (int): Number of initial candidates to fetch
        rerank_top_n (int): Number of reranked results to return
        
    Returns:
        Dict[str, Any]: Combined results with reranking scores
    """
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=pinecone_api_key)
        index = pc.Index(index_name)
        
        # Step 1: Initial similarity search
        print(f"🔍 Step 1: Initial similarity search (top {initial_top_k})...")
        initial_results = index.query(
            vector=query_embedding,
            top_k=initial_top_k,
            include_metadata=True
        )
        
        candidates = initial_results.get('matches', [])
        if not candidates:
            print("No candidates found for reranking")
            return {"matches": []}
        
        print(f"✅ Found {len(candidates)} initial candidates")
        
        # Step 2: Prepare documents for reranking
        print(f"🔄 Step 2: Standalone reranking using {rerank_model}...")
        documents = []
        for match in candidates:
            metadata = match.get('metadata', {})
            chunk_text = metadata.get('chunk_text', '')
            
            # Create document for reranking
            doc = {
                "id": match.get('id', ''),
                "chunk_text": chunk_text
            }
            documents.append(doc)
        
        # Step 3: Rerank using Pinecone's inference API
        rerank_results = pc.inference.rerank(
            model=rerank_model,
            query=query_text,
            documents=documents,
            top_n=rerank_top_n,
            rank_fields=["chunk_text"],
            return_documents=True
        )
        
        # Step 4: Combine reranking results with original metadata
        combined_results = []
        for rerank_item in rerank_results.data:
            # Find the original match
            original_match = candidates[rerank_item.index]
            
            # Create combined result
            combined_result = {
                "id": original_match.get('id', ''),
                "score": original_match.get('score', 0),  # Original similarity score
                "rerank_score": rerank_item.score,  # Reranking relevance score
                "metadata": original_match.get('metadata', {}),
                "rerank_index": rerank_item.index
            }
            combined_results.append(combined_result)
        
        print(f"✅ Reranked to top {len(combined_results)} most relevant results")
        
        return {
            "matches": combined_results,
            "rerank_model": rerank_model,
            "usage": rerank_results.usage
        }
        
    except Exception as e:
        error_msg = str(e)
        if "PERMISSION_DENIED" in error_msg or "not authorized" in error_msg:
            print(f"❌ Error: Pinecone account not authorized for reranking models")
            print("💡 Solutions:")
            print("   1. Check your Pinecone plan - reranking may require paid/higher tier")
            print("   2. Contact Pinecone support to enable reranking models")
            print("   3. Use alternative reranking approaches:")
            print(f"      - Basic search: python scripts/search_pinecone.py \"{query_text}\"")
            print(f"      - Direct Cohere: python scripts/search_with_reranking.py \"{query_text}\"")
            print("   4. Check Pinecone documentation for account requirements")
        else:
            print(f"❌ Error in standalone reranking search: {e}")
        raise


def format_integrated_results(results: Dict[str, Any], show_full_text: bool = False) -> None:
    """
    Format and display integrated reranking results.
    
    Args:
        results (Dict[str, Any]): Results from integrated reranking search
        show_full_text (bool): Whether to show full chunk text or just preview
    """
    matches = results.get('matches', [])
    
    if not matches:
        print("No results found.")
        return
    
    print(f"\n🔍 Integrated Reranking Results ({len(matches)} matches)")
    print("=" * 80)
    
    for i, match in enumerate(matches, 1):
        score = match.get('score', 0)  # This is the reranking score for integrated results
        metadata = match.get('metadata', {})
        
        print(f"\n📄 Result {i} (Relevance Score: {score:.4f})")
        print("-" * 50)
        
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
        
        if i < len(matches):
            print("\n" + "─" * 50)


def format_standalone_results(results: Dict[str, Any], show_full_text: bool = False) -> None:
    """
    Format and display standalone reranking results.
    
    Args:
        results (Dict[str, Any]): Results from standalone reranking search
        show_full_text (bool): Whether to show full chunk text or just preview
    """
    matches = results.get('matches', [])
    rerank_model = results.get('rerank_model', 'unknown')
    
    if not matches:
        print("No results found.")
        return
    
    print(f"\n🔍 Standalone Reranking Results ({len(matches)} matches)")
    print(f"Model: {rerank_model}")
    print("=" * 80)
    
    for i, match in enumerate(matches, 1):
        similarity_score = match.get('score', 0)
        rerank_score = match.get('rerank_score', 0)
        metadata = match.get('metadata', {})
        
        print(f"\n📄 Result {i}")
        print("-" * 50)
        print(f"Similarity: {similarity_score:.4f} | Relevance: {rerank_score:.4f}")
        
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
        
        if i < len(matches):
            print("\n" + "─" * 50)


def interactive_search(pinecone_api_key: str, index_name: str, openai_api_key: str):
    """
    Interactive search mode where user can test different reranking approaches.
    
    Args:
        pinecone_api_key (str): Pinecone API key
        index_name (str): Name of the Pinecone index
        openai_api_key (str): OpenAI API key
    """
    print("\n🔄 Interactive Pinecone Reranking Mode")
    print("Test both integrated and standalone reranking approaches")
    print("=" * 65)
    
    available_models = [
        "cohere-rerank-3.5",
        "bge-reranker-v2-m3", 
        "pinecone-rerank-v0"
    ]
    
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
            print(f"\nAvailable models: {', '.join(available_models)}")
            model_input = input("Reranking model (default: cohere-rerank-3.5): ").strip()
            model = model_input if model_input in available_models else "cohere-rerank-3.5"
            
            method_input = input("Method - 'integrated' or 'standalone' (default: integrated): ").strip()
            method = method_input if method_input in ['integrated', 'standalone'] else 'integrated'
            
            try:
                top_k_input = input("Initial candidates (default 20): ").strip()
                initial_top_k = int(top_k_input) if top_k_input else 20
            except ValueError:
                initial_top_k = 20
                
            try:
                top_n_input = input("Final results (default 5): ").strip()
                rerank_top_n = int(top_n_input) if top_n_input else 5
            except ValueError:
                rerank_top_n = 5
                
            show_full = input("Show full text? (y/N): ").strip().lower() == 'y'
            
            # Perform search based on chosen method
            if method == 'integrated':
                # Integrated reranking uses Pinecone's text query API
                results = search_with_integrated_reranking(
                    query, pinecone_api_key, index_name, 
                    model, initial_top_k, rerank_top_n
                )
                format_integrated_results(results, show_full_text=show_full)
            else:
                # Standalone reranking uses traditional embedding search + separate reranking
                query_embedding = generate_query_embedding(query, openai_api_key)
                results = search_with_standalone_reranking(
                    query, query_embedding, pinecone_api_key, index_name,
                    model, initial_top_k, rerank_top_n
                )
                format_standalone_results(results, show_full_text=show_full)
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error during search: {e}")
            continue


def main():
    """Main function to handle command-line arguments and perform search."""
    parser = argparse.ArgumentParser(
        description="Search Pinecone index with hosted reranking models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/search_with_pinecone_reranking.py "machine learning"
  python scripts/search_with_pinecone_reranking.py --query "docker" --model cohere-rerank-3.5 --method standalone
  python scripts/search_with_pinecone_reranking.py --interactive
  python scripts/search_with_pinecone_reranking.py "OpenAI API" --full-text --method integrated

Available Models:
  - cohere-rerank-3.5: Cohere's leading reranking model (default)
  - bge-reranker-v2-m3: Multilingual reranking model
  - pinecone-rerank-v0: Pinecone's state-of-the-art model
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
        '--model',
        type=str,
        default='cohere-rerank-3.5',
        choices=['cohere-rerank-3.5', 'bge-reranker-v2-m3', 'pinecone-rerank-v0'],
        help='Pinecone-hosted reranking model to use (default: cohere-rerank-3.5)'
    )
    
    parser.add_argument(
        '--method',
        type=str,
        default='integrated',
        choices=['integrated', 'standalone'],
        help='Reranking method: integrated (part of search) or standalone (separate operation) (default: integrated)'
    )
    
    parser.add_argument(
        '--initial-top-k',
        type=int,
        default=20,
        help='Number of initial candidates to fetch (default: 20)'
    )
    
    parser.add_argument(
        '--rerank-top-n',
        type=int,
        default=5,
        help='Number of final results after reranking (default: 5)'
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
    
    print("Pinecone Hosted Reranking Search")
    print("=" * 40)
    
    # Load environment variables
    load_environment()
    
    # Get required environment variables
    pinecone_api_key, index_name, openai_api_key = get_required_env_vars()
    
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
        interactive_search(pinecone_api_key, index_name, openai_api_key)
        return
    
    # Get query from arguments
    query = args.query or args.query_flag

    if not query:
        print("❌ Error: Please provide a search query")
        print("Use --help for usage examples")
        return
    
    try:
        # Note: For integrated reranking, Pinecone handles embedding generation internally
        
        # Perform search based on chosen method
        if args.method == 'integrated':
            print(f"\n🔄 Using integrated reranking with {args.model}")
            results = search_with_integrated_reranking(
                query, pinecone_api_key, index_name,
                args.model, args.initial_top_k, args.rerank_top_n
            )
            format_integrated_results(results, show_full_text=args.full_text)
        else:
            print(f"\n🔄 Using standalone reranking with {args.model}")
            # Generate query embedding for standalone method
            query_embedding = generate_query_embedding(query, openai_api_key)
            results = search_with_standalone_reranking(
                query, query_embedding, pinecone_api_key, index_name,
                args.model, args.initial_top_k, args.rerank_top_n
            )
            format_standalone_results(results, show_full_text=args.full_text)
        
    except Exception as e:
        print(f"❌ Search failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()