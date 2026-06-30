from jarvis import Jarvis
from modules.commands import *

assistant = Jarvis()

while True:
    command = input("You: ")
    command = command.lower()
    if "bye" in command:
        goodbye()
        break
    else:
        assistant.process_command(command)
    

    

