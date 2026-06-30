from pathlib import Path

# -----------------------------
# Project Root
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# -----------------------------
# Directories
# -----------------------------

DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"

# Automatically create directories
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# -----------------------------
# JSON Files
# -----------------------------

MEMORY_FILE = DATA_DIR / "memory.json"
TASK_FILE = DATA_DIR / "tasks.json"
CHAT_HISTORY_FILE = DATA_DIR / "chat_history.json"

# -----------------------------
# Log File
# -----------------------------

LOG_FILE = LOG_DIR / "jarvis.log"