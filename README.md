# TLDR

Welcome to Vector Search Reranking in 10 minutes

## High level steps

- Create a DB index
- Seed the Vector DB
- Perform similarity search
- Rerank initial results
- Take a subset of your reranked results
- RAG

## Link to Pinecone

https://pinecone.io/

## Scripts Directory

This directory contains modular Python scripts for processing markdown files with front matter and chunking content for embedding workflows.

## Core Module

### `markdown_processor.py`
**Reusable module** containing all the core functionality for processing markdown files. This module can be imported by any script in the project.

**Key Functions:**
- `extract_front_matter_and_content()` - Extract YAML front matter from markdown
- `setup_text_splitter()` - Configure LangChain TokenTextSplitter 
- `process_markdown_file()` - Process a single markdown file
- `process_multiple_markdown_files()` - Batch process files in a directory
- `get_processing_stats()` - Calculate processing statistics
- `save_processed_data_to_json()` - Save results to JSON file

## Scripts

### `process_markdown_files.py`
**Main processing script** that uses the modular functions to process all markdown files in the `raw_data` folder. Optimized for Ada 002 embedding workflow.

Usage:
```bash
python scripts/process_markdown_files.py
```

### `example_usage.py`
**Documentation script** showing various ways to use the modular functions in other scripts.

Usage:
```bash
python scripts/example_usage.py
```

## Usage Examples

### Import the module in your own scripts:

```python
from pathlib import Path
from markdown_processor import (
    setup_text_splitter,
    process_markdown_file,
    process_multiple_markdown_files
)

# Process a single file
splitter = setup_text_splitter(chunk_size=1000, encoding_name="cl100k_base")
result = process_markdown_file(Path("example.md"), splitter)

# Batch process files
results = process_multiple_markdown_files(Path("./data"))

# Extract just front matter
from markdown_processor import extract_front_matter_and_content
with open("file.md") as f:
    front_matter, content = extract_front_matter_and_content(f.read())
```

### Different tokenizer encodings for various models:

- **Ada 002, GPT-3.5, GPT-4**: `"cl100k_base"`
- **Older GPT models**: `"gpt2"`
- **Codex models**: `"p50k_base"`

### `delete_pinecone_index.py`
**Pinecone management script** that connects to your Pinecone index and deletes all vectors, effectively clearing the index.

Usage:
```bash
python scripts/delete_pinecone_index.py
```

### `insert_into_pinecone.py`
**Complete pipeline script** that:
1. Processes all markdown files using the modular functions
2. Generates embeddings using OpenAI's Ada 002 model  
3. Inserts embedded chunks into Pinecone with rich metadata

Usage:
```bash
python scripts/insert_into_pinecone.py
```

### `test_small_insert.py`
**Test script** that processes only the 3 smallest files to test the pipeline without hitting API quota limits.

Usage:
```bash
python scripts/test_small_insert.py
```

### `search_pinecone.py`
**Similarity search script** that allows you to query your Pinecone index to find the most similar content chunks.

Usage:
```bash
# Basic search
python scripts/search_pinecone.py "machine learning"

# Advanced search with options
python scripts/search_pinecone.py --query "docker deployment" --top-k 3 --full-text

# Interactive mode
python scripts/search_pinecone.py --interactive
```

## Environment Setup

Create a `.env` file in the project root with your API keys:

```bash
# Create .env file in project root
cat > .env << EOF
# Pinecone Configuration
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_INDEX_NAME=your-index-name

# OpenAI Configuration  
OPENAI_API_KEY=your-openai-api-key-here
EOF

# Then edit with your actual API keys
```

**Required Environment Variables:**
- `PINECONE_API_KEY` - Your Pinecone API key
- `PINECONE_INDEX_NAME` - Name of your Pinecone index  
- `OPENAI_API_KEY` - Your OpenAI API key for Ada 002 embeddings

## Search Examples

Once you have data in your Pinecone index, you can search it in multiple ways:

```bash
# Basic search for machine learning content
python scripts/search_pinecone.py "machine learning"

# Search for Docker-related content with more results
python scripts/search_pinecone.py --query "docker deployment" --top-k 10

# Show full text instead of previews
python scripts/search_pinecone.py "OpenAI API" --full-text

# Interactive mode for multiple searches
python scripts/search_pinecone.py --interactive

# Search for specific technologies
python scripts/search_pinecone.py "vector database"
python scripts/search_pinecone.py "Flask Python"
python scripts/search_pinecone.py "React TypeScript"
```

## Complete Workflow

Here's the typical workflow for processing markdown files and inserting into Pinecone:

```bash
# 1. Set up environment variables
cat > .env << EOF
PINECONE_API_KEY=your-actual-api-key
PINECONE_INDEX_NAME=reranking-vectors
OPENAI_API_KEY=your-actual-openai-key
EOF

# 2. (Recommended) Test with small sample first
python scripts/test_small_insert.py

# 3. (Optional) Clear existing data from Pinecone index
python scripts/delete_pinecone_index.py

# 4. Process ALL markdown files and insert into Pinecone with embeddings
python scripts/insert_into_pinecone.py

# 5. Search your index for similar content
python scripts/search_pinecone.py "your search query"

# 6. (Optional) Process files standalone for analysis
python scripts/process_markdown_files.py
```

**What each script does:**
- **`test_small_insert.py`** → Test pipeline with 3 smallest files (recommended first)
- **`delete_pinecone_index.py`** → Clears all vectors from your index
- **`insert_into_pinecone.py`** → Full pipeline: chunk → embed → insert (all files)
- **`search_pinecone.py`** → Query your index to find similar content chunks
- **`process_markdown_files.py`** → Process and analyze files locally

## Dependencies

Required packages (already in `pyproject.toml`):
- `langchain-text-splitters>=0.3.0`
- `pyyaml>=6.0`
- `tiktoken>=0.5.0`
- `pinecone>=3.0.0`
- `openai>=1.0.0`
- `python-dotenv>=1.0.0`