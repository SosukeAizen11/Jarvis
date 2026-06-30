import os

class AppManager:

    def __init__(self):
        self.apps = {
            "chrome": "chrome",
            "vscode": "code",
            "notepad": "notepad.exe",
            "calculator": "calc.exe"
        }

    def open_app(self, app_name):
        if app_name in self.apps:
            os.startfile(self.apps[app_name])