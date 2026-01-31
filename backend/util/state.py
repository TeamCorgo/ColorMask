from datetime import datetime


class User:
    def __init__(self, username: str):
        self.username: str = username
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")
        self.x: int = 0
        self.y: int = 0
        self.universe: str = "0"


class Cell:
    def __init__(self, color: str):
        self.color: str = color
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")
        self.owner: "User | None" = None


class AppState:
    def __init__(self):
        self.users = {}
        self.themes = {}
        self.seed = "f2a61844"
        self.auth_tokens = {}


STATE = AppState()
