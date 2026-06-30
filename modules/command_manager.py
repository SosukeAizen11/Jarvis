from modules.commands import *

class CommandManager:
    def __init__(
            self,
            memory_manager,
            game_manager,
            music_manager,
            search_engine,
            calculator,
            todo_manager,
            file_manager,
            app_manager,
            ai_manager
    ):
        self.memory_manager = memory_manager
        self.game_manager = game_manager
        self.music_manager = music_manager
        self.search_engine = search_engine
        self.calculator = calculator
        self.todo_manager = todo_manager
        self.file_manager = file_manager
        self.app_manager = app_manager
        self.ai_manager = ai_manager

    def process(self, command):

        commands = {
            "hello": greet,
            "introduce": introduce,

            "google": opengoogle,
            "youtube": openyoutube,
            "github": opengithub,

            "time": telltime,
            "date": telldate,
            "day": tellday,

            "flip coin": self.game_manager.flip_coin,
            "roll dice": self.game_manager.roll_dice,

            "list files": self.file_manager.list_files,
        }


        if command in commands:
            return commands[command]()

        elif "help me" in command:
            return self.show_help()

        elif command.startswith("what is"):
            words = command.split()
            key = " ".join(words[2:])

            value = self.memory_manager.recall(key)

            if value:
                return value
            else:
                return self.ai_manager.ask(command)

        elif command.startswith("search"):
            words = command.split()
            query = " ".join(words[1:])
            self.search_engine.search_google(query)
            return f"Searching Google for {query}"

        elif command.startswith("calculate"):
            words = command.split()
            expression = " ".join(words[1:])
            answer = self.calculator.calculate(expression)
            return str(answer)

        elif command.startswith("play song"):
            words = command.split()
            song = " ".join(words[2:])
            self.music_manager.play_song(song)
            return f"Playing {song}"

        elif command.startswith("add task"):
            words = command.split()
            task = " ".join(words[2:])
            return self.todo_manager.add_task(task)
            

        elif command.startswith("remove task"):
            words = command.split()
            index = int(words[2])
            return self.todo_manager.remove_task(index)
           
        elif command.startswith("create file"):
            words = command.split()
            filename = " ".join(words[2:])
            self.file_manager.create_file(filename)
            return f"{filename} created."

        elif command.startswith("delete file"):
            words = command.split()
            filename = " ".join(words[2:])
            self.file_manager.delete_file(filename)
            return f"{filename} deleted."

        elif command.startswith("open"):
            words = command.split()
            app_name = " ".join(words[1:])
            self.app_manager.open_app(app_name)
            return f"Opening {app_name}"

        elif command.startswith("ask"):
            words = command.split()
            prompt = " ".join(words[1:])
            return self.ai_manager.ask(prompt)
        
        elif command == "start game":
            return self.game_manager.start_guess_game()
        
        elif command.startswith("guess"):
            words = command.split()
            if len(words) != 2:
                return "Usage: guess <number>"
            try:
                number = int(words[1])
                return self.game_manager.guess_number(number)
            except ValueError:
                return "Please enter a valid number."
            
        elif command == "stop game":
            return self.game_manager.stop_guess_game()
        
        elif command == "show tasks":
            return self.todo_manager.show_tasks()
        
        decision = self.ai_manager.should_remember(command)

        if decision == "YES":
            key, value = self.ai_manager.extract_memory(command)
            self.memory_manager.remember(key, value)
            return "I'll remember that!"
        
        return "Sorry, I don't understand that command."

    def show_help(self):

        available_commands = [
            "hello",
            "introduce",
            "google",
            "youtube",
            "github",
            "time",
            "date",
            "day",
            "ask ...",
            "open ...",
            "add task ...",
            "remove task ..."
        ]

        return "\n".join(
            f"{i}. {command}"
            for i, command in enumerate(available_commands, start=1)
        )