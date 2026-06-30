from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# -----------------------------
# Application
# -----------------------------

APP_NAME = "Jarvis"

VERSION = "1.0.0"

# -----------------------------
# AI
# -----------------------------

DEFAULT_MODEL = "llama-3.3-70b-versatile"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -----------------------------
# Memory
# -----------------------------

MAX_CHAT_HISTORY = 20