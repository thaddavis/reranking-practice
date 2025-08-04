# TLDR

Info related to how we can seed a Vector DB

##

I downloaded the transcripts for the top 16 most-watched videso on the COMMAND YouTube channel using this tool: https://tactiq.io/tools/run/youtube_transcript. I stored the transcripts into the `raw_data` folder

##

I then experimented with chunking the text in various ways by installing `uv` ie: I vibe coded the `process_markdown_files.py` script

##

Peep the following scripts...

- insert_into_pinecone.py
- delete_pinecone_index.py
