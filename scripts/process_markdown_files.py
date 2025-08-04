#!/usr/bin/env python3
"""
Script to process markdown files from raw_data folder.

This script:
1. Loops through all markdown files in the raw_data folder
2. Extracts front matter (YAML metadata) from each file
3. Chunks the content using LangChain's TokenTextSplitter
4. Outputs processed data for further use with embedding models like Ada 002

Usage:
    python scripts/process_markdown_files.py
"""

from pathlib import Path
from markdown_processor import (
    setup_text_splitter,
    process_multiple_markdown_files,
    get_processing_stats
)


def main():
    """Main function to process all markdown files in the raw_data folder."""
    
    # Set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    raw_data_dir = project_root / "raw_data"
    
    if not raw_data_dir.exists():
        print(f"Error: raw_data directory not found at {raw_data_dir}")
        return
    
    # Set up the text splitter
    # Configuration optimized for Ada 002 embedding model
    text_splitter = setup_text_splitter(
        chunk_size=1000,      # Good size for Ada 002 (max 8191 tokens)
        chunk_overlap=200,    # 20% overlap to maintain context
        encoding_name="cl100k_base"  # Ada 002 uses this encoding
    )
    
    # Process all markdown files using the modular function
    print(f"Processing markdown files in {raw_data_dir}...")
    all_processed_data = process_multiple_markdown_files(
        directory_path=raw_data_dir,
        text_splitter=text_splitter,
        include_chunk_previews=True
    )
    
    if not all_processed_data:
        print(f"No markdown files found in {raw_data_dir}")
        return
    
    print(f"Found {len(all_processed_data)} markdown files to process...")
    print("-" * 60)
    
    # Print detailed results for each file
    for processed_data in all_processed_data:
        print(f"Processing: {processed_data['file_name']}")
        
        # Print summary for this file
        if 'error' not in processed_data:
            front_matter = processed_data['front_matter']
            print(f"  Title: {front_matter.get('video_title', 'N/A')}")
            print(f"  URL: {front_matter.get('video_url', 'N/A')}")
            print(f"  Original length: {processed_data['original_content_length']:,} characters")
            print(f"  Number of chunks: {processed_data['num_chunks']}")
            
            # Show chunk info if available
            if 'chunk_info' in processed_data:
                for chunk_info in processed_data['chunk_info']:
                    print(f"    Chunk {chunk_info['chunk_index']}: {chunk_info['chunk_length']} chars")
                    print(f"      Preview: {chunk_info['chunk_preview']}")
        else:
            print(f"  ERROR: {processed_data['error']}")
        
        print("-" * 60)
    
    # Print summary statistics using the modular function
    stats = get_processing_stats(all_processed_data)
    
    print(f"\nPROCESSING SUMMARY:")
    print(f"Total files processed: {stats['total_files']}")
    print(f"Successful: {stats['successful_files']}")
    print(f"Failed: {stats['failed_files']}")
    print(f"Total chunks created: {stats['total_chunks']}")
    print(f"Average chunks per file: {stats['avg_chunks_per_file']:.1f}")
    print(f"Success rate: {stats['success_rate']:.1%}")
    
    # Optional: Save processed data to a file for later use
    # You could uncomment this section to save the data as JSON for embedding later
    """
    from markdown_processor import save_processed_data_to_json
    output_file = project_root / "processed_data.json"
    save_processed_data_to_json(all_processed_data, output_file)
    print(f"\nProcessed data saved to: {output_file}")
    """
    
    return all_processed_data


if __name__ == "__main__":
    main()