from modules.ai_manager import AIManager
import json


class Brain:

    def __init__(self):

        self.ai = AIManager()

    # ---------------------------------------------------
    # Intent Detection
    # ---------------------------------------------------

    def classify(self, command: str) -> str:

        command = command.lower().strip()

        # ----------------------------
        # Fast Commands
        # ----------------------------

        known_commands = (
            "hello",
            "introduce",
            "google",
            "youtube",
            "github",
            "time",
            "date",
            "day",
            "flip coin",
            "roll dice",
            "guess number",
            "show tasks",
            "list files",
        )

        if command in known_commands:
            return "COMMAND"

        if command.startswith("add task"):
            return "ADD_TASK"

        if command.startswith("remove task"):
            return "REMOVE_TASK"

        if command.startswith("open"):
            return "OPEN_APP"

        if command.startswith("search"):
            return "SEARCH"

        if command.startswith("calculate"):
            return "CALCULATE"
        
        if command.startswith("create file"):
            return "COMMAND"

        if command.startswith("delete file"):
            return "COMMAND"

        if command.startswith("play song"):
            return "COMMAND"

        if command.startswith("ask"):
            return "COMMAND"

        if command.startswith("start game"):
            return "COMMAND"

        if command.startswith("guess"):
            return "COMMAND"

        if command.startswith("stop game"):
            return "COMMAND"

        # ----------------------------
        # AI Classification
        # ----------------------------

        messages = [
            {
                "role": "system",
                "content":
                """
You are Jarvis's Brain.

Your job is ONLY to classify intent.

Return ONLY one of:

MEMORY_STORE
MEMORY_QUERY
GENERAL_AI
"""
            },
            {
                "role": "user",
                "content": command
            }
        ]

        intent = self.ai.generate(messages)
        print(f"[DEBUG] Brain returned = {intent!r}")
        return intent.strip()

    # ---------------------------------------------------
    # Should Remember
    # ---------------------------------------------------

    def should_remember(self, text: str) -> bool:

        messages = [
            {
                "role": "system",
                "content":
                """
Decide whether this information should be stored as long-term memory.

Respond ONLY:

YES

or

NO
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]

        answer = self.ai.generate(messages)

        return answer.strip() == "YES"

    # ---------------------------------------------------
    # Extract Memory
    # ---------------------------------------------------

    def extract_memory(self, text: str) -> tuple[str, str]:

        messages = [
            {
                "role": "system",
                "content":
                """
Extract a key and value.

Return ONLY JSON.

Example

{
    "key":"idol",
    "value":"Cristiano Ronaldo"
}
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]

        answer = self.ai.generate(messages)

        memory = json.loads(answer)

        return memory["key"], memory["value"]