import json

from modules.base_manager import BaseManager
from config.logger import get_logger
from config.paths import MEMORY_FILE

logger = get_logger(__name__)


class MemoryManager(BaseManager):

    def __init__(self):
        super().__init__("Memory Manager")

        self.memory: dict[str, str] = {}

        self.load_memory()

    def remember(self, key: str, value: str) -> str:

        self.memory[key] = value

        self.save_memory()

        logger.info(f"Memory saved: {key}")

        return "I will remember that!"

    def recall(self, key: str) -> str | None:

        if key in self.memory:

            logger.info(f"Memory recalled: {key}")

            return f"{key} is {self.memory[key]}"

        logger.warning(f"Memory not found: {key}")

        return None

    def load_memory(self) -> None:

        try:

            with MEMORY_FILE.open("r") as file:

                self.memory = json.load(file)

            logger.info("Memory loaded successfully.")

        except FileNotFoundError:

            logger.warning("Memory file not found. Creating a new one.")

            self.memory = {}

            self.save_memory()

    def save_memory(self) -> None:

        with MEMORY_FILE.open("w") as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

        logger.info("Memory written to disk.")