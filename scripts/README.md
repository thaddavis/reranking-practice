# Scripts Directory

This directory contains modular Python scripts for processing markdown files with front matter and chunking content for embedding workflows, including advanced similarity search with re-ranking.

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

## Data Management Scripts

### `process_markdown_files.py`
**Main processing script** that uses the modular functions to process all markdown files in the `raw_data` folder. Optimized for Ada 002 embedding workflow.

Usage:
```bash
python scripts/process_markdown_files.py
```

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

## Search Scripts

### `search_pinecone.py`
**Basic similarity search script** that queries your Pinecone index to find the most similar content chunks using embedding similarity.

Usage:
```bash
# Basic search
python scripts/search_pinecone.py "machine learning"

# Advanced search with options
python scripts/search_pinecone.py --query "docker deployment" --top-k 3 --full-text

# Interactive mode
python scripts/search_pinecone.py --interactive
```

### `search_with_reranking.py` 🏆
**Advanced search with re-ranking** that:
1. Performs initial similarity search using embeddings
2. Re-ranks results using Cohere's state-of-the-art re-ranking model (via Cohere client)
3. Returns the most relevant results with both similarity and relevance scores

Usage:
```bash
# Basic re-ranking search
python scripts/search_with_reranking.py "machine learning"

# Advanced re-ranking with custom parameters
python scripts/search_with_reranking.py --query "docker deployment" --initial-top-k 15 --rerank-top-k 3

# Interactive re-ranking mode
python scripts/search_with_reranking.py --interactive
```

### `search_with_pinecone_reranking.py` 🆕
**Search with Pinecone's hosted reranking models** that:
1. Uses Pinecone's hosted reranking endpoints (no separate Cohere API key needed)
2. Supports both integrated and standalone reranking approaches
3. Multiple hosted models: Cohere 3.5, BGE reranker, and Pinecone's own model

Usage:
```bash
# Integrated reranking (reranking as part of search query)
python scripts/search_with_pinecone_reranking.py "machine learning"

# Standalone reranking (separate reranking operation)
python scripts/search_with_pinecone_reranking.py --query "docker" --method standalone

# Use different reranking models
python scripts/search_with_pinecone_reranking.py "AI" --model pinecone-rerank-v0

# Interactive mode to test different approaches
python scripts/search_with_pinecone_reranking.py --interactive
```

**⚠️ Note**: Pinecone's hosted reranking models may require a paid Pinecone plan. If you get permission errors, use the direct Cohere reranking script instead.

**Re-ranking Benefits:**
- **Higher Precision**: Re-ranking models understand semantic relevance better than pure similarity
- **Better Results**: Often surfaces more relevant results that pure embedding similarity might miss
- **Dual Scoring**: Shows both embedding similarity and semantic relevance scores
- **Hosted Convenience**: Pinecone-hosted models require only Pinecone API key (no separate Cohere key)

### `compare_search_methods.py` 🆕
**Comparison tool** that runs the same query through both basic similarity search and re-ranking search, displaying results side-by-side to show the differences.

Usage:
```bash
# Compare search methods for a query
python scripts/compare_search_methods.py "machine learning"

# Compare with custom number of results
python scripts/compare_search_methods.py --query "docker deployment" --num-results 3
```

### `example_usage.py`
**Documentation script** showing various ways to use the modular functions in other scripts.

Usage:
```bash
python scripts/example_usage.py
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

# Cohere Configuration (for direct Cohere reranking)
COHERE_API_KEY=your-cohere-api-key-here
EOF

# Then edit with your actual API keys
```

**Required Environment Variables:**
- `PINECONE_API_KEY` - Your Pinecone API key
- `PINECONE_INDEX_NAME` - Name of your Pinecone index  
- `OPENAI_API_KEY` - Your OpenAI API key for Ada 002 embeddings
- `COHERE_API_KEY` - Your Cohere API key (only needed for `search_with_reranking.py`)

## Search Comparison Examples

**Basic Similarity Search:**
```bash
python scripts/search_pinecone.py "vector database" --top-k 5
# Returns: Top 5 results based on embedding similarity
```

**Re-ranking Search (Direct Cohere - Recommended):**
```bash
python scripts/search_with_reranking.py "vector database" --initial-top-k 15 --rerank-top-k 5
# Returns: Top 5 most relevant results from 15 candidates, re-ranked by Cohere
```

**Re-ranking Search (Pinecone Hosted):**
```bash
python scripts/search_with_pinecone_reranking.py "vector database" --method integrated
# Returns: Results re-ranked using Pinecone's hosted Cohere model (requires paid plan)
```

The re-ranking approach typically provides more semantically relevant results by:
1. Casting a wider net with initial similarity search (15-20 candidates)
2. Using advanced language models to re-rank based on true semantic relevance
3. Returning the most relevant subset

**Pinecone Hosted vs. Direct Cohere:**
- **Pinecone Hosted**: Simpler setup (only Pinecone API key), integrated infrastructure
  - ⚠️ May require paid Pinecone plan for reranking model access
- **Direct Cohere**: More control, separate billing, requires additional API key
  - ✅ Works with any Pinecone plan (uses separate Cohere account)

## Complete Workflow

Here's the typical workflow for processing markdown files and searching with re-ranking:

```bash
# 1. Set up environment variables
cat > .env << EOF
PINECONE_API_KEY=your-actual-api-key
PINECONE_INDEX_NAME=reranking-vectors
OPENAI_API_KEY=your-actual-openai-key
COHERE_API_KEY=your-actual-cohere-key
EOF

# 2. (Recommended) Test with small sample first
python scripts/test_small_insert.py

# 3. (Optional) Clear existing data from Pinecone index
python scripts/delete_pinecone_index.py

# 4. Process ALL markdown files and insert into Pinecone with embeddings
python scripts/insert_into_pinecone.py

# 5. Search with advanced re-ranking for best results
# Option A: Direct Cohere reranking (recommended - works with any plan)
python scripts/search_with_reranking.py "your search query"

# Option B: Pinecone-hosted reranking (if available on your Pinecone plan)
python scripts/search_with_pinecone_reranking.py "your search query"

# 6. (Optional) Compare search methods side-by-side
python scripts/compare_search_methods.py "your search query"

# 7. (Alternative) Basic similarity search only
python scripts/search_pinecone.py "your search query"

# 8. (Optional) Process files standalone for analysis
python scripts/process_markdown_files.py
```

**What each script does:**
- **`test_small_insert.py`** → Test pipeline with 3 smallest files (recommended first)
- **`delete_pinecone_index.py`** → Clears all vectors from your index
- **`insert_into_pinecone.py`** → Full pipeline: chunk → embed → insert (all files)
- **`search_with_reranking.py`** → **🏆 Advanced search with direct Cohere re-ranking (recommended)**
- **`search_with_pinecone_reranking.py`** → Pinecone-hosted reranking (requires paid plan)
- **`search_pinecone.py`** → Basic similarity search using embeddings only
- **`compare_search_methods.py`** → Side-by-side comparison of search methods
- **`process_markdown_files.py`** → Process and analyze files locally

## Dependencies

Required packages (already in `pyproject.toml`):
- `langchain-text-splitters>=0.3.0`
- `pyyaml>=6.0`
- `tiktoken>=0.5.0`
- `pinecone>=3.0.0`
- `openai>=1.0.0`
- `python-dotenv>=1.0.0`
- `cohere>=5.0.0` (for re-ranking functionality)

## Getting API Keys

### Cohere API Key (Recommended for Re-ranking)

To use the direct Cohere re-ranking functionality:

1. **Sign up for Cohere**: Visit [cohere.ai](https://cohere.ai) and create an account
2. **Get API key**: Go to your dashboard and generate an API key
3. **Add to .env**: Set `COHERE_API_KEY=your-cohere-api-key` in your `.env` file

Cohere offers free tier usage that's perfect for testing and moderate usage of the re-ranking functionality.

### Pinecone Hosted Re-ranking

For Pinecone's hosted reranking models:

1. **Check your plan**: Hosted reranking may require a paid Pinecone plan
2. **Contact support**: If you get permission errors, contact Pinecone support
3. **Alternative**: Use the direct Cohere approach which works with any Pinecone plan

## Recommended Approach

For most users, we recommend using the **direct Cohere re-ranking** approach:

```bash
# Recommended: Direct Cohere re-ranking
python scripts/search_with_reranking.py "your query here"
```

This approach:
- ✅ Works with any Pinecone plan (free or paid)
- ✅ Gives you full control over the re-ranking process
- ✅ Uses the latest Cohere re-ranking models
- ✅ Provides transparent billing (separate Cohere account)