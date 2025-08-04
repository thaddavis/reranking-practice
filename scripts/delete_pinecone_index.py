#!/usr/bin/env python3
"""
Script to delete all data from a Pinecone index.

This script connects to a Pinecone index and deletes all vectors,
effectively clearing the index for fresh data insertion.

Usage:
    python scripts/delete_pinecone_index.py

Environment Variables Required:
    PINECONE_API_KEY - Your Pinecone API key
    PINECONE_INDEX_NAME - Name of the Pinecone index to clear
"""

import os
import sys
from pathlib import Path
from pinecone import Pinecone
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
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")
    
    missing_vars = []
    if not api_key:
        missing_vars.append("PINECONE_API_KEY")
    if not index_name:
        missing_vars.append("PINECONE_INDEX_NAME")
    
    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these in your .env file or environment.")
        print("Example .env file:")
        print("PINECONE_API_KEY=your-api-key-here")
        print("PINECONE_INDEX_NAME=your-index-name")
        sys.exit(1)
    
    return api_key, index_name


def delete_all_vectors_from_index(api_key: str, index_name: str, confirm: bool = True):
    """
    Delete all vectors from a Pinecone index.
    
    Args:
        api_key (str): Pinecone API key
        index_name (str): Name of the index to clear
        confirm (bool): Whether to ask for confirmation before deletion
    """
    try:
        # Initialize Pinecone client
        pc = Pinecone(api_key=api_key)
        
        # Get the index
        print(f"Connecting to Pinecone index: {index_name}")
        index = pc.Index(index_name)
        
        # Get index stats before deletion
        stats = index.describe_index_stats()
        total_vectors = stats.get('total_vector_count', 0)
        
        print(f"Index '{index_name}' currently contains {total_vectors:,} vectors")
        
        if total_vectors == 0:
            print("✅ Index is already empty!")
            return
        
        # Confirmation prompt
        if confirm:
            print(f"\n⚠️  WARNING: This will delete ALL {total_vectors:,} vectors from the index!")
            print(f"Index: {index_name}")
            response = input("Are you sure you want to continue? (yes/no): ").lower().strip()
            
            if response not in ['yes', 'y']:
                print("❌ Operation cancelled by user")
                return
        
        # Delete all vectors
        print("\n🗑️  Deleting all vectors from index...")
        
        # Use delete_all which is more efficient for clearing entire index
        index.delete(delete_all=True)
        
        print("✅ All vectors deleted successfully!")
        
        # Verify deletion
        print("\n🔍 Verifying deletion...")
        stats_after = index.describe_index_stats()
        remaining_vectors = stats_after.get('total_vector_count', 0)
        
        if remaining_vectors == 0:
            print(f"✅ Verification complete: Index '{index_name}' is now empty")
        else:
            print(f"⚠️  Warning: {remaining_vectors} vectors still remain (may take a moment to update)")
            
    except Exception as e:
        print(f"❌ Error deleting vectors from index: {e}")
        sys.exit(1)


def main():
    """Main function to delete all data from Pinecone index."""
    print("Pinecone Index Deletion Script")
    print("=" * 40)
    
    # Load environment variables
    load_environment()
    
    # Get required environment variables
    api_key, index_name = get_required_env_vars()
    
    # Delete all vectors
    delete_all_vectors_from_index(api_key, index_name, confirm=True)
    
    print("\n✅ Script completed successfully!")


if __name__ == "__main__":
    main()