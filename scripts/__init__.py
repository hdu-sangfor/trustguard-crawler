"""RAG corpus preprocessing scripts.

Tools for cleaning raw cybersecurity documents and splitting them into
retrieval-ready chunks for vector database ingestion.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = PROJECT_ROOT / "doc"
CLEAN_DIR = PROJECT_ROOT / "clean"
CHUNKS_DIR = PROJECT_ROOT / "chunks"
