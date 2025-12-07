import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

EMBED_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1"
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing! Add it to your .env file.")
