from datetime import datetime


class User:
    def __init__(self, username: str):
        self.username = username
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")
        self.x = 0
        self.y = 0
        self.universe: "User | None" = None


class Cell:
    def __init__(self, color: str):
        self.color = color
        self.created = datetime.now().strftime("%Y.%m.%d %H:%M")
        self.owner: "User | None" = None


class AppState:
    def __init__(self):
        self.users = {}
        self.themes = {}
        self.seed = "f2a61844"
        self.auth_tokens = {}


STATE = AppState()
