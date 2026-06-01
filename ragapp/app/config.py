"""Central configuration. Reads environment variables from .env."""
import os
from dotenv import load_dotenv

load_dotenv(".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "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")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

# Embedding model — small, fast, runs locally on CPU.
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Where the FAISS vector index is persisted on disk.
VECTORSTORE_DIR = "data/vectorstore"

# Chunking parameters: balances context and retrieval precision.
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# How many chunks to retrieve per query.
TOP_K = 4
