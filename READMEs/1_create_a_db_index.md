# TLDR

Notes related to creating a DB index for demonstrating re-ranking

## Create a new index in Pinecone

1. Create an index called `text-embedding-ada-002`
1. Configuration
  - Vector type: `Dense`
  - Dimension: `1536`
  - Metric: `cosine`
  - Capacity mode: `serverless`
  - Cloud provider: `aws`
  - Region: `us-east-1`
1. Click create