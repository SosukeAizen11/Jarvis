import json

from groq import Groq

from config.logger import get_logger
from config.paths import CHAT_HISTORY_FILE
from config.settings import DEFAULT_MODEL, GROQ_API_KEY

logger = get_logger(__name__)


class AIManager:

    def __init__(self):

        self.client = Groq(api_key=GROQ_API_KEY)

        self.messages: list[dict[str, str]] = []

        self.load_messages()

    # ---------------------------------------------------
    # Low Level LLM Call
    # ---------------------------------------------------

    def generate(self, messages: list[dict[str, str]]) -> str:

        response = self.client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages
        )

        return response.choices[0].message.content

    # ---------------------------------------------------
    # Chat
    # ---------------------------------------------------

    def ask(self, prompt: str) -> str:

        self.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        answer = self.generate(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        self.save_messages()

        logger.info("AI response generated.")

        return answer

    # ---------------------------------------------------
    # Save Chat
    # ---------------------------------------------------

    def save_messages(self) -> None:

        with CHAT_HISTORY_FILE.open("w") as file:

            json.dump(
                self.messages,
                file,
                indent=4
            )

        logger.info("Chat history saved.")

    # ---------------------------------------------------
    # Load Chat
    # ---------------------------------------------------

    def load_messages(self) -> None:

        try:

            with CHAT_HISTORY_FILE.open("r") as file:

                self.messages = json.load(file)

            logger.info("Chat history loaded.")

        except FileNotFoundError:

            logger.warning("Chat history not found.")

            self.messages = [
                {
                    "role": "system",
                    "content": "You are Jarvis, a helpful AI assistant."
                }
            ]

            self.save_messages()