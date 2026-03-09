import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

VECTOR_DB_PATH = "vectorstore"
DOCUMENT_PATH = "data/documents"