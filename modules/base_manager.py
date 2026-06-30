class BaseManager:
    
    def __init__(self, name):
        self.name = name
        print(f"{self.name} initialized")
        
    def show_info(self):
        print(f"I am {self.name}")