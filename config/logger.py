import logging

from config.paths import LOG_FILE

# -----------------------------
# Configure Logging
# -----------------------------

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE,
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

# -----------------------------
# Logger Factory
# -----------------------------

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)