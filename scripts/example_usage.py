#!/usr/bin/env python3
"""
Example script demonstrating how to use the modular markdown processing functions.

This shows various ways other scripts in the project can leverage the markdown_processor module.
"""

from pathlib import Path
from markdown_processor import (
    extract_front_matter_and_content,
    setup_text_splitter,
    process_markdown_file,
    process_multiple_markdown_files,
    get_processing_stats,
    save_processed_data_to_json
)


def example_1_process_single_file():
    """Example: Process a single markdown file with custom settings."""
    print("=== Example 1: Processing a single file ===")
    
    # Setup custom text splitter
    splitter = setup_text_splitter(
        chunk_size=500,        # Smaller chunks
        chunk_overlap=100,     # Less overlap
        encoding_name="cl100k_base"
    )
    
    # Process one file
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    sample_file = raw_data_dir / "What_is_Ollama_glkQIUTCAK4.md"
    
    if sample_file.exists():
        result = process_markdown_file(sample_file, splitter, include_chunk_previews=False)
        
        print(f"File: {result['file_name']}")
        print(f"Title: {result['front_matter'].get('video_title', 'N/A')}")
        print(f"Chunks created: {result['num_chunks']}")
        print(f"Original length: {result['original_content_length']} chars")
        print()


def example_2_extract_front_matter_only():
    """Example: Just extract front matter from files without chunking."""
    print("=== Example 2: Extract front matter only ===")
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    
    for md_file in sorted(raw_data_dir.glob("*.md"))[:3]:  # Just first 3 files
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        front_matter, main_content = extract_front_matter_and_content(content)
        
        print(f"File: {md_file.name}")
        print(f"  Title: {front_matter.get('video_title', 'N/A')}")
        print(f"  URL: {front_matter.get('video_url', 'N/A')}")
        print(f"  Content length: {len(main_content)} chars")
        print()


def example_3_batch_process_with_stats():
    """Example: Batch process files and get detailed statistics."""
    print("=== Example 3: Batch processing with statistics ===")
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    
    # Process with different settings
    splitter = setup_text_splitter(chunk_size=800, chunk_overlap=150)
    
    results = process_multiple_markdown_files(
        directory_path=raw_data_dir,
        text_splitter=splitter,
        include_chunk_previews=False  # Skip previews for faster processing
    )
    
    stats = get_processing_stats(results)
    
    print(f"Processed {stats['total_files']} files")
    print(f"Success rate: {stats['success_rate']:.1%}")
    print(f"Total chunks: {stats['total_chunks']}")
    print(f"Average chunks per file: {stats['avg_chunks_per_file']:.1f}")
    print(f"Average content length: {stats['avg_content_length']:.0f} chars")
    print()


def example_4_save_to_json():
    """Example: Process files and save results to JSON for later use."""
    print("=== Example 4: Save processed data to JSON ===")
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    output_file = Path(__file__).parent.parent / "example_processed_data.json"
    
    # Quick processing of a subset
    splitter = setup_text_splitter(chunk_size=600, chunk_overlap=100)
    
    # Process only files with "Ollama" in the name
    ollama_files = [f for f in raw_data_dir.glob("*.md") if "Ollama" in f.name]
    
    results = []
    for file_path in ollama_files:
        result = process_markdown_file(file_path, splitter)
        results.append(result)
    
    if results:
        save_processed_data_to_json(results, output_file)
        print(f"Saved {len(results)} processed files to {output_file}")
        
        # Clean up the example file
        output_file.unlink()
        print("Example file cleaned up")
    else:
        print("No Ollama files found")
    print()


def example_5_different_encodings():
    """Example: Using different tokenizer encodings for different models."""
    print("=== Example 5: Different tokenizer encodings ===")
    
    raw_data_dir = Path(__file__).parent.parent / "raw_data"
    sample_file = raw_data_dir / "Performance_Testing_Fastify_vs_Express-7TUZjl-hjro.md"
    
    if not sample_file.exists():
        print("Sample file not found")
        return
    
    # Different encodings for different models
    encodings = {
        "Ada 002 / GPT-3.5 / GPT-4": "cl100k_base",
        "Older GPT models": "gpt2", 
        "Codex models": "p50k_base"
    }
    
    for model_name, encoding in encodings.items():
        splitter = setup_text_splitter(
            chunk_size=500,
            encoding_name=encoding
        )
        
        result = process_markdown_file(sample_file, splitter)
        print(f"{model_name} ({encoding}): {result['num_chunks']} chunks")
    
    print()


def main():
    """Run all examples."""
    print("Markdown Processor Module Usage Examples")
    print("=" * 50)
    print()
    
    example_1_process_single_file()
    example_2_extract_front_matter_only()
    example_3_batch_process_with_stats()
    example_4_save_to_json()
    example_5_different_encodings()
    
    print("All examples completed!")


if __name__ == "__main__":
    main()