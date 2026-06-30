import customtkinter as ctk
import threading
from jarvis import Jarvis

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Backend
        self.assistant = Jarvis()

        # Window
        self.title("Jarvis")
        self.geometry("800x600")

        # Chatbox
        self.chatbox = ctk.CTkTextbox(
            self,
            font=("Arial", 14)
        )
        self.chatbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # Input frame
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=10
        )

        # Entry
        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter command..."
        )
        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        # Send button
        self.send_button = ctk.CTkButton(
            self.input_frame,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack(side="right")

        # Enter key support
        self.entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

    def send_message(self):

        command = self.entry.get().strip()

        if not command:
            return

        # Display user message
        self.chatbox.insert(
            "end",
            f"You: {command}\n\n"
        )
        
        self.chatbox.see("end")

        # Clear input box
        self.entry.delete(0, "end")

        # Disable button while processing
        self.send_button.configure(state="disabled")
        self.entry.configure(state="disabled")
        
        thread = threading.Thread(
            target=self.process_command,
            args=(command,),
            daemon=True
        )
        thread.start()
    
    def process_command(self, command):
        response = self.assistant.process_command(command)
        # Schedule GUI update on the main thread
        self.after(
            0,
            self.display_response,
            response
        )
        
    def display_response(self, response):
        if response:
            self.chatbox.insert(
                "end",
                f"Jarvis: {response}\n\n"
            )
        self.chatbox.see("end")
        
        self.send_button.configure(state="normal")
        self.entry.configure(state="normal")
        self.entry.focus()
        


if __name__ == "__main__":
    app = App()
    app.mainloop()