# Vector Search Reranking in 10 Minutes

A complete RAG (Retrieval-Augmented Generation) pipeline with advanced reranking capabilities for processing markdown files, generating embeddings, and performing intelligent similarity search with semantic reranking.

## Quick Start (TLDR)

**High-level workflow:**
1. Create a Pinecone index
2. Process and chunk markdown files
3. Generate embeddings and seed the vector database
4. Perform similarity search
5. **Rerank results for better relevance** 🎯
6. Use reranked results for RAG applications

**Quick demo:**
```bash
# Set up environment
cp .env.example .env  # Add your API keys

# Test with small sample
python scripts/test_small_insert.py

# Search with reranking (best results)
python scripts/search_with_reranking.py "machine learning"
```

## What This Project Does

This project provides a **production-ready RAG pipeline** that:

- 📄 **Processes markdown files** with YAML front matter extraction
- 🔢 **Chunks content** using LangChain's TokenTextSplitter (optimized for Ada 002)
- 🎯 **Generates embeddings** using OpenAI's `text-embedding-ada-002` model
- 📚 **Stores vectors** in Pinecone with rich metadata
- 🔍 **Performs similarity search** with multiple approaches
- 🏆 **Reranks results** using state-of-the-art models for better relevance
- ⚖️ **Compares search methods** side-by-side

## Key Features

### 🎯 **Multiple Search Approaches**
- **Basic Similarity**: Fast embedding-based search
- **Direct Cohere Reranking** 🏆: Advanced semantic reranking (recommended)
- **Pinecone Hosted Reranking**: Integrated reranking (requires paid plan)
- **Side-by-side Comparison**: See the difference reranking makes

### 🛠️ **Production Ready**
- Modular, reusable functions
- Comprehensive error handling
- Rate limiting and batch processing
- Interactive and scriptable modes
- Rich metadata preservation

## Installation & Setup

### 1. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

### 2. Environment Configuration

Create a `.env` file in the project root:

```bash
cat > .env << EOF
# Pinecone Configuration
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_INDEX_NAME=your-index-name

# OpenAI Configuration  
OPENAI_API_KEY=your-openai-api-key-here

# Cohere Configuration (for reranking - recommended)
COHERE_API_KEY=your-cohere-api-key-here
EOF
```

**Required APIs:**
- **Pinecone**: [pinecone.io](https://pinecone.io) - Vector database
- **OpenAI**: [platform.openai.com](https://platform.openai.com) - Embeddings
- **Cohere**: [cohere.ai](https://cohere.ai) - Reranking (free tier available)

## Complete Workflow

### Step-by-Step Pipeline

```bash
# 1. Test with small sample first (recommended)
python scripts/test_small_insert.py

# 2. (Optional) Clear existing data
python scripts/delete_pinecone_index.py

# 3. Process ALL files and insert into Pinecone
python scripts/insert_into_pinecone.py

# 4. Search with reranking (best results) 🏆
python scripts/search_with_reranking.py "your search query"

# 5. (Optional) Compare search methods
python scripts/compare_search_methods.py "your search query"
```

### Alternative Search Options

```bash
# Basic similarity search (fastest)
python scripts/search_pinecone.py "vector database"

# Advanced reranking search (best relevance) 🏆
python scripts/search_with_reranking.py "vector database" --initial-top-k 15 --rerank-top-k 5

# Pinecone hosted reranking (requires paid plan)
python scripts/search_with_pinecone_reranking.py "vector database"

# Compare methods side-by-side
python scripts/compare_search_methods.py "vector database"

# Interactive search mode
python scripts/search_with_reranking.py --interactive
```

## Scripts Overview

### **Core Module**
- **`scripts/markdown_processor.py`** → Reusable module with all processing functions

### **Data Management**
- **`scripts/test_small_insert.py`** → Test pipeline with 3 smallest files ⭐ (start here)
- **`scripts/insert_into_pinecone.py`** → Full pipeline: process → embed → insert
- **`scripts/delete_pinecone_index.py`** → Clear all vectors from index
- **`scripts/process_markdown_files.py`** → Process files locally (no Pinecone)

### **Search & Reranking**
- **`scripts/search_with_reranking.py`** → **🏆 Advanced Cohere reranking (recommended)**
- **`scripts/search_pinecone.py`** → Basic similarity search
- **`scripts/search_with_pinecone_reranking.py`** → Pinecone hosted reranking
- **`scripts/compare_search_methods.py`** → Side-by-side comparison tool

### **Examples & Documentation**
- **`scripts/example_usage.py`** → Code examples for using the module

## Search Examples

### Basic Search
```bash
# Simple search
python scripts/search_pinecone.py "machine learning"

# More results with full text
python scripts/search_pinecone.py "docker deployment" --top-k 10 --full-text
```

### Advanced Reranking (Recommended) 🏆
```bash
# Basic reranking - significantly better results
python scripts/search_with_reranking.py "machine learning"

# Custom parameters for fine-tuning
python scripts/search_with_reranking.py \
  --query "docker kubernetes deployment" \
  --initial-top-k 20 \
  --rerank-top-k 5

# Interactive mode for experimentation
python scripts/search_with_reranking.py --interactive
```

### Compare Search Methods
```bash
# See the difference reranking makes
python scripts/compare_search_methods.py "vector database"
```

## Why Reranking?

**Traditional similarity search** uses embedding cosine similarity, which sometimes misses nuanced semantic relationships.

**Reranking** uses advanced language models to understand true semantic relevance:

1. **Cast a wide net**: Fetch 15-20 candidates with similarity search
2. **Intelligent ranking**: Use Cohere's reranking model to understand semantic relevance  
3. **Better results**: Return the most actually relevant content

**Results:**
- 🎯 **Higher precision** - More relevant results
- 🧠 **Better semantics** - Understands context and intent
- 📊 **Dual scoring** - Shows both similarity and relevance scores

## API Key Setup

### Cohere (Recommended for Reranking)

1. Visit [cohere.ai](https://cohere.ai) and create a free account
2. Go to your dashboard and generate an API key
3. Add `COHERE_API_KEY=your-key-here` to your `.env` file

**Why Cohere?**
- ✅ Free tier available for testing
- ✅ State-of-the-art reranking models
- ✅ Works with any Pinecone plan
- ✅ Transparent pricing

### Pinecone vs. Direct Cohere

| Approach | Setup | Cost | Performance | Recommendation |
|----------|-------|------|-------------|----------------|
| **Direct Cohere** | Separate API key | Pay per use | Latest models | **🏆 Recommended** |
| **Pinecone Hosted** | Single API key | Included in plan | Integrated | Requires paid plan |

## Programming Examples

### Using the Core Module

```python
from pathlib import Path
from scripts.markdown_processor import (
    setup_text_splitter,
    process_markdown_file,
    process_multiple_markdown_files
)

# Process a single file
splitter = setup_text_splitter(chunk_size=1000, encoding_name="cl100k_base")
result = process_markdown_file(Path("example.md"), splitter)

# Batch process files
results = process_multiple_markdown_files(Path("./raw_data"))

# Extract front matter
from scripts.markdown_processor import extract_front_matter_and_content
with open("file.md") as f:
    front_matter, content = extract_front_matter_and_content(f.read())
```

### Tokenizer Options

Choose the right encoding for your embedding model:

- **Ada 002, GPT-3.5, GPT-4**: `"cl100k_base"` (default)
- **Older GPT models**: `"gpt2"`
- **Codex models**: `"p50k_base"`

## Dependencies

All dependencies are managed in `pyproject.toml`:

```toml
dependencies = [
    "langchain-text-splitters>=0.3.0",
    "pyyaml>=6.0",
    "tiktoken>=0.5.0",
    "pinecone>=3.0.0",
    "openai>=1.0.0",
    "python-dotenv>=1.0.0",
    "cohere>=5.0.0",
]
```

## Data Structure

The pipeline processes markdown files from `raw_data/` with the following structure:

```
raw_data/
├── video1.md    # YAML front matter + content
├── video2.md    # Automatically chunked
└── ...
```

Each file includes rich metadata:
- Video title and URL
- File information
- Chunk indices and content
- Processing timestamps

## Troubleshooting

### Common Issues

**"Permission denied" for Pinecone reranking:**
```bash
# Use direct Cohere instead
python scripts/search_with_reranking.py "your query"
```

**OpenAI quota exceeded:**
```bash
# Test with smaller sample first
python scripts/test_small_insert.py
```

**Import errors:**
```bash
# Install in development mode
pip install -e .
```

## Project Structure

```
reranking/
├── README.md                      # This file
├── pyproject.toml                 # Dependencies
├── .env                          # API keys (create this)
├── raw_data/                     # Source markdown files
├── scripts/
│   ├── markdown_processor.py     # Core module
│   ├── test_small_insert.py      # ⭐ Start here
│   ├── insert_into_pinecone.py   # Full pipeline
│   ├── search_with_reranking.py  # 🏆 Best search
│   ├── search_pinecone.py        # Basic search
│   ├── compare_search_methods.py # Comparison tool
│   └── ...                       # Other utilities
└── READMEs/                      # Additional documentation
```

## What's Next?

1. **🚀 Start here**: `python scripts/test_small_insert.py`
2. **🔍 Search**: `python scripts/search_with_reranking.py "your query"`
3. **📊 Compare**: `python scripts/compare_search_methods.py "your query"`
4. **🛠️ Customize**: Modify chunk sizes, models, or add new functionality

---

**Ready to get started?** Run the test script and start searching! 🎯