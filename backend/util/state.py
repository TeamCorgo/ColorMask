from datetime import datetime


class User:
    def __init__(self, username: str):
        self.username: str = username
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")
        self.color: str = "#000000"
        self.x: int = 0
        self.y: int = 0
        self.universe: str = "0"


class Cell:
    def __init__(self, color: str):
        self.color: str = color
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")


class AppState:
    def __init__(self):
        self.users = {}
        self.themes = {}
        self.seed = "corgo844"
        self.auth_tokens = {}
        self.cells = {}


STATE = AppState()
