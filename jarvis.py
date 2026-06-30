from modules.commands import *
from modules.memory_manager import MemoryManager
from modules.game_manager import GameManager
from modules.music_manager import MusicManager
from modules.search_engine import SearchEngine
from modules.calculator import Calculator
from modules.todo_manager import TodoManager
from modules.file_manager import FileManager
from modules.app_manager import AppManager
from modules.ai_manager import AIManager
from modules.command_manager import CommandManager
from modules.brain import Brain

class Jarvis:
    def __init__(self):
        
        self.memory_manager = MemoryManager()
        self.game_manager = GameManager()
        self.music_manager = MusicManager()
        self.search_engine = SearchEngine()
        self.calculator = Calculator()
        self.todo_manager = TodoManager()
        self.file_manager = FileManager()
        self.app_manager = AppManager()
        self.ai_manager = AIManager()
        self.brain = Brain()  
        
        self.command_manager = CommandManager(
            self.memory_manager,
            self.game_manager,
            self.music_manager,
            self.search_engine,
            self.calculator,
            self.todo_manager,
            self.file_manager,
            self.app_manager,
            self.ai_manager
        )
    
    def process_command(self, command):
        intent = self.brain.classify(command)

        print(f"[DEBUG] Intent = {intent!r}")

        if intent == "COMMAND":
            return self.command_manager.process(command)
        elif intent == "GENERAL_AI":
            print("[DEBUG] Calling AIManager.ask()")
            return self.ai_manager.ask(command)
        else:
            print("[DEBUG] Unknown intent")
            return f"Unknown intent: {intent}"