#!/usr/bin/env python3
"""
Script to compare basic similarity search vs. re-ranking search results.

This script runs the same query through both search methods and displays
the results side-by-side to show the difference in ranking and relevance.

Usage:
    python scripts/compare_search_methods.py "your search query"
    python scripts/compare_search_methods.py --query "machine learning" --num-results 3

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
from typing import List, Dict, Any
from pinecone import Pinecone
import openai
import cohere
from dotenv import load_dotenv

# Import functions from our other scripts
sys.path.append(str(Path(__file__).parent))
from search_pinecone import generate_query_embedding, search_pinecone_index, load_environment, get_required_env_vars as get_basic_env_vars
from search_with_reranking import rerank_with_cohere, get_required_env_vars as get_rerank_env_vars


def compare_search_results(
    query: str,
    pinecone_api_key: str,
    index_name: str,
    openai_api_key: str,
    cohere_api_key: str,
    num_results: int = 5
):
    """
    Compare basic similarity search vs re-ranking search for the same query.
    
    Args:
        query (str): Search query
        pinecone_api_key (str): Pinecone API key
        index_name (str): Pinecone index name
        openai_api_key (str): OpenAI API key
        cohere_api_key (str): Cohere API key
        num_results (int): Number of results to compare
    """
    try:
        print(f"🔍 Comparing search methods for query: '{query}'")
        print("=" * 80)
        
        # Generate query embedding (same for both methods)
        print("\n1️⃣ Generating query embedding...")
        query_embedding = generate_query_embedding(query, openai_api_key)
        
        # Method 1: Basic similarity search
        print(f"\n2️⃣ Basic Similarity Search (top {num_results})...")
        basic_results = search_pinecone_index(
            query_embedding, 
            pinecone_api_key, 
            index_name, 
            top_k=num_results
        )
        basic_matches = basic_results.get('matches', [])
        
        # Method 2: Re-ranking search
        print(f"\n3️⃣ Re-ranking Search (from top 20, re-ranked to {num_results})...")
        rerank_candidates = search_pinecone_index(
            query_embedding, 
            pinecone_api_key, 
            index_name, 
            top_k=20  # Get more candidates for re-ranking
        )
        candidates = rerank_candidates.get('matches', [])
        
        if candidates:
            reranked_results = rerank_with_cohere(
                query, 
                candidates, 
                cohere_api_key, 
                top_k=num_results
            )
        else:
            reranked_results = []
        
        # Display comparison
        print("\n" + "=" * 80)
        print("📊 RESULTS COMPARISON")
        print("=" * 80)
        
        print(f"\n{'BASIC SIMILARITY SEARCH':<40} | {'RE-RANKING SEARCH':<40}")
        print("-" * 40 + " | " + "-" * 40)
        
        # Show results side by side
        max_results = max(len(basic_matches), len(reranked_results))
        
        for i in range(max_results):
            # Basic result
            if i < len(basic_matches):
                basic_match = basic_matches[i]
                basic_metadata = basic_match.get('metadata', {})
                basic_title = basic_metadata.get('video_title', 'Unknown')[:35]
                basic_score = basic_match.get('score', 0)
                basic_info = f"{i+1}. {basic_title} ({basic_score:.3f})"
            else:
                basic_info = ""
            
            # Re-ranked result
            if i < len(reranked_results):
                rerank_match = reranked_results[i]
                rerank_metadata = rerank_match.get('metadata', {})
                rerank_title = rerank_metadata.get('video_title', 'Unknown')[:35]
                rerank_relevance = rerank_match.get('rerank_relevance_score', 0)
                rerank_similarity = rerank_match.get('original_similarity_score', 0)
                rerank_info = f"{i+1}. {rerank_title} (R:{rerank_relevance:.3f}|S:{rerank_similarity:.3f})"
            else:
                rerank_info = ""
            
            print(f"{basic_info:<40} | {rerank_info:<40}")
        
        # Analysis
        print("\n" + "=" * 80)
        print("📈 ANALYSIS")
        print("=" * 80)
        
        if basic_matches and reranked_results:
            # Check how many results are the same in top positions
            same_top_3 = 0
            for i in range(min(3, len(basic_matches), len(reranked_results))):
                basic_id = basic_matches[i].get('id', '')
                rerank_id = reranked_results[i].get('id', '')
                if basic_id == rerank_id:
                    same_top_3 += 1
            
            print(f"• Same results in top 3 positions: {same_top_3}/3")
            print(f"• Re-ranking potentially improved relevance by reordering results")
            print(f"• Similarity scores range: {basic_matches[-1].get('score', 0):.3f} - {basic_matches[0].get('score', 0):.3f}")
            
            if reranked_results:
                relevance_scores = [r.get('rerank_relevance_score', 0) for r in reranked_results]
                print(f"• Relevance scores range: {min(relevance_scores):.3f} - {max(relevance_scores):.3f}")
        
        print("\n💡 Key Differences:")
        print("• Basic Search: Ranks by embedding similarity only")
        print("• Re-ranking: Uses semantic understanding for better relevance")
        print("• R: Relevance Score | S: Similarity Score")
        
    except Exception as e:
        print(f"❌ Error during comparison: {e}")
        raise


def main():
    """Main function to handle command-line arguments and perform comparison."""
    parser = argparse.ArgumentParser(
        description="Compare basic similarity search vs re-ranking search",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/compare_search_methods.py "machine learning"
  python scripts/compare_search_methods.py --query "docker deployment" --num-results 3
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
        '--num-results',
        type=int,
        default=5,
        help='Number of results to compare (default: 5)'
    )
    
    args = parser.parse_args()
    
    print("Search Methods Comparison Tool")
    print("=" * 35)
    
    # Load environment variables
    load_environment()
    
    # Get required environment variables (needs all for re-ranking)
    try:
        pinecone_api_key, index_name, openai_api_key, cohere_api_key = get_rerank_env_vars()
    except SystemExit:
        print("\n💡 Note: This script requires all API keys including Cohere for comparison.")
        print("If you only have basic search keys, use search_pinecone.py instead.")
        return
    
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
    
    # Get query from arguments
    query = args.query or args.query_flag

    if not query:
        print("❌ Error: Please provide a search query")
        print("Use --help for usage examples")
        return
    
    try:
        # Perform comparison
        compare_search_results(
            query,
            pinecone_api_key,
            index_name,
            openai_api_key,
            cohere_api_key,
            num_results=args.num_results
        )
        
    except Exception as e:
        print(f"❌ Comparison failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()