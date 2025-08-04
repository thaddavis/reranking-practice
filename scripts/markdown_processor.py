"""
Markdown processing utilities for extracting front matter and chunking content.

This module provides reusable functions for processing markdown files with YAML front matter
and splitting content into chunks using LangChain's TokenTextSplitter.
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from langchain_text_splitters import TokenTextSplitter


def extract_front_matter_and_content(file_content: str) -> Tuple[Dict[str, Any], str]:
    """
    Extract YAML front matter and main content from a markdown file.
    
    Args:
        file_content (str): The full content of the markdown file
        
    Returns:
        Tuple[Dict[str, Any], str]: Front matter as dict and main content as string
        
    Example:
        >>> content = "---\\ntitle: Test\\n---\\nContent here"
        >>> front_matter, content = extract_front_matter_and_content(content)
        >>> front_matter['title']
        'Test'
        >>> content
        'Content here'
    """
    # Pattern to match YAML front matter between --- delimiters
    front_matter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(front_matter_pattern, file_content, re.DOTALL)
    
    if match:
        yaml_content = match.group(1)
        main_content = match.group(2)
        
        try:
            front_matter = yaml.safe_load(yaml_content)
            return front_matter or {}, main_content.strip()
        except yaml.YAMLError as e:
            print(f"Error parsing YAML front matter: {e}")
            return {}, file_content.strip()
    else:
        # No front matter found, treat entire content as main content
        return {}, file_content.strip()


def setup_text_splitter(
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    encoding_name: str = "cl100k_base"
) -> TokenTextSplitter:
    """
    Set up a LangChain TokenTextSplitter with specified parameters.
    
    Args:
        chunk_size (int): Maximum number of tokens per chunk
        chunk_overlap (int): Number of tokens to overlap between chunks
        encoding_name (str): Tokenizer encoding to use
                           - "cl100k_base" for Ada 002, GPT-3.5, GPT-4
                           - "gpt2" for older models
                           - "p50k_base" for Codex models
        
    Returns:
        TokenTextSplitter: Configured text splitter instance
        
    Example:
        >>> splitter = setup_text_splitter(chunk_size=500, chunk_overlap=50)
        >>> chunks = splitter.split_text("Your long text here...")
    """
    return TokenTextSplitter(
        encoding_name=encoding_name,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )


def process_markdown_file(
    file_path: Path, 
    text_splitter: TokenTextSplitter,
    include_chunk_previews: bool = True,
    preview_length: int = 100
) -> Dict[str, Any]:
    """
    Process a single markdown file by extracting front matter and chunking content.
    
    Args:
        file_path (Path): Path to the markdown file
        text_splitter (TokenTextSplitter): Configured text splitter
        include_chunk_previews (bool): Whether to include chunk preview text
        preview_length (int): Length of preview text for each chunk
        
    Returns:
        Dict[str, Any]: Processed file data with metadata and chunks
        
    Example:
        >>> from pathlib import Path
        >>> splitter = setup_text_splitter()
        >>> result = process_markdown_file(Path("example.md"), splitter)
        >>> print(f"File has {result['num_chunks']} chunks")
    """
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        # Extract front matter and content
        front_matter, main_content = extract_front_matter_and_content(file_content)
        
        # Split the content into chunks
        text_chunks = text_splitter.split_text(main_content)
        
        # Prepare the processed data
        processed_data = {
            'file_name': file_path.name,
            'file_path': str(file_path),
            'front_matter': front_matter,
            'original_content_length': len(main_content),
            'num_chunks': len(text_chunks),
            'chunks': text_chunks,
        }
        
        # Add chunk info if requested
        if include_chunk_previews:
            processed_data['chunk_info'] = [
                {
                    'chunk_index': i,
                    'chunk_length': len(chunk),
                    'chunk_preview': chunk[:preview_length] + "..." if len(chunk) > preview_length else chunk
                }
                for i, chunk in enumerate(text_chunks)
            ]
        
        return processed_data
        
    except Exception as e:
        return {
            'file_name': file_path.name,
            'file_path': str(file_path),
            'error': str(e),
            'front_matter': {},
            'chunks': [],
            'num_chunks': 0
        }


def process_multiple_markdown_files(
    directory_path: Path,
    text_splitter: Optional[TokenTextSplitter] = None,
    file_pattern: str = "*.md",
    include_chunk_previews: bool = True
) -> List[Dict[str, Any]]:
    """
    Process multiple markdown files in a directory.
    
    Args:
        directory_path (Path): Path to directory containing markdown files
        text_splitter (Optional[TokenTextSplitter]): Text splitter to use.
                                                   If None, creates default splitter
        file_pattern (str): Glob pattern for files to process
        include_chunk_previews (bool): Whether to include chunk preview text
        
    Returns:
        List[Dict[str, Any]]: List of processed file data
        
    Example:
        >>> from pathlib import Path
        >>> results = process_multiple_markdown_files(Path("./raw_data"))
        >>> print(f"Processed {len(results)} files")
    """
    if not directory_path.exists():
        raise ValueError(f"Directory not found: {directory_path}")
    
    if text_splitter is None:
        text_splitter = setup_text_splitter()
    
    # Find all markdown files
    markdown_files = list(directory_path.glob(file_pattern))
    
    if not markdown_files:
        return []
    
    # Process each file
    processed_files = []
    for file_path in sorted(markdown_files):
        processed_data = process_markdown_file(
            file_path, 
            text_splitter,
            include_chunk_previews=include_chunk_previews
        )
        processed_files.append(processed_data)
    
    return processed_files


def get_processing_stats(processed_files: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate statistics from a list of processed markdown files.
    
    Args:
        processed_files (List[Dict[str, Any]]): List of processed file data
        
    Returns:
        Dict[str, Any]: Statistics about the processing results
        
    Example:
        >>> results = process_multiple_markdown_files(Path("./data"))
        >>> stats = get_processing_stats(results)
        >>> print(f"Average chunks per file: {stats['avg_chunks_per_file']}")
    """
    total_files = len(processed_files)
    successful_files = [f for f in processed_files if 'error' not in f]
    failed_files = [f for f in processed_files if 'error' in f]
    
    total_chunks = sum(f['num_chunks'] for f in successful_files)
    total_content_length = sum(f.get('original_content_length', 0) for f in successful_files)
    
    return {
        'total_files': total_files,
        'successful_files': len(successful_files),
        'failed_files': len(failed_files),
        'total_chunks': total_chunks,
        'avg_chunks_per_file': total_chunks / len(successful_files) if successful_files else 0,
        'total_content_length': total_content_length,
        'avg_content_length': total_content_length / len(successful_files) if successful_files else 0,
        'success_rate': len(successful_files) / total_files if total_files > 0 else 0
    }


def save_processed_data_to_json(
    processed_files: List[Dict[str, Any]], 
    output_path: Path,
    indent: int = 2
) -> None:
    """
    Save processed markdown data to a JSON file.
    
    Args:
        processed_files (List[Dict[str, Any]]): List of processed file data
        output_path (Path): Path where to save the JSON file
        indent (int): JSON indentation level
        
    Example:
        >>> results = process_multiple_markdown_files(Path("./data"))
        >>> save_processed_data_to_json(results, Path("processed_data.json"))
    """
    import json
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(processed_files, f, indent=indent, ensure_ascii=False)