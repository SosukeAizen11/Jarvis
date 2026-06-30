import json

from modules.base_manager import BaseManager
from config.logger import get_logger
from config.paths import TASK_FILE

logger = get_logger(__name__)


class TodoManager(BaseManager):

    def __init__(self):
        super().__init__("Todo Manager")

        self.tasks: list[str] = []

        self.load_tasks()

    # ------------------------
    # Add Task
    # ------------------------

    def add_task(self, task: str) -> str:

        self.tasks.append(task)

        self.save_tasks()

        logger.info(f"Task added: {task}")

        return "Task added successfully."

    # ------------------------
    # Show Tasks
    # ------------------------

    def show_tasks(self) -> str:

        if not self.tasks:

            logger.info("No tasks available.")

            return "No tasks available."

        logger.info("Displaying task list.")

        result = "Tasks:\n\n"

        for i, task in enumerate(self.tasks, start=1):

            result += f"{i}. {task}\n"

        return result

    # ------------------------
    # Remove Task
    # ------------------------

    def remove_task(self, index: int) -> str:

        if index < 1 or index > len(self.tasks):

            logger.warning(f"Invalid task number: {index}")

            return "Invalid task number."

        removed_task = self.tasks.pop(index - 1)

        self.save_tasks()

        logger.info(f"Task removed: {removed_task}")

        return f"Removed task: {removed_task}"

    # ------------------------
    # Save Tasks
    # ------------------------

    def save_tasks(self) -> None:

        with TASK_FILE.open("w") as file:

            json.dump(
                self.tasks,
                file,
                indent=4
            )

        logger.info("Tasks saved to disk.")

    # ------------------------
    # Load Tasks
    # ------------------------

    def load_tasks(self) -> None:

        try:

            with TASK_FILE.open("r") as file:

                self.tasks = json.load(file)

            logger.info("Tasks loaded successfully.")

        except FileNotFoundError:

            logger.warning("Task file not found. Creating a new one.")

            self.tasks = []

            self.save_tasks()