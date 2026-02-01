import json
import os


def reserved_universe_names() -> list:
    return [
        "0",
        "Admin",
        "Hunter",
        "Corgo",
        "Corgo LC",
        "Lord Corgo",
        "United States of America",
        "Earth",
    ]


def save_users(users: dict) -> None:
    for username, user in users.items():
        file_path = f"/storage/users/{username}.json"
        with open(file_path, "w") as file:
            json.dump(user, file, default=vars, indent=4)
    return


def save_cells(cells: dict) -> None:
    for cord, cell in cells.items():
        file_path = f"/storage/cells/{cord}.json"
        with open(file_path, "w") as file:
            json.dump(cell, file, default=vars, indent=4)
    return


def save_tokens(auth_tokens: dict) -> None:
    for username, token in auth_tokens.items():
        file_path = f"/storage/tokens/{username}.json"
        with open(file_path, "w") as file:
            json.dump({"token": token}, file, indent=4)
    return


def save_themes(themes: dict) -> None:
    filepath = "/storage/themes.json"
    with open(filepath, "w") as file:
        json.dump(themes, file, indent=4)
    return


def load_users() -> dict:
    users = {}
    user_dir = "/storage/users/"
    # Iterate over all JSON files in the directory
    for filename in os.listdir(user_dir):
        if filename.endswith(".json"):
            username = filename[:-5]  # remove ".json"
            file_path = os.path.join(user_dir, filename)
            with open(file_path, "r") as file:
                users[username] = json.load(file)
    return users


def load_cells() -> dict:
    cells = {}
    cells_dir = "/storage/users/"
    # Iterate over all JSON files in the directory
    for filename in os.listdir(cells_dir):
        if filename.endswith(".json"):
            cell = filename[:-5]  # remove ".json"
            file_path = os.path.join(cells_dir, filename)
            with open(file_path, "r") as file:
                cells[cell] = json.load(file)
    return cells


def load_tokens() -> dict:
    tokens = {}
    tokens_dir = "/storage/users/"
    # Iterate over all JSON files in the directory
    for filename in os.listdir(tokens_dir):
        if filename.endswith(".json"):
            token = filename[:-5]  # remove ".json"
            file_path = os.path.join(tokens_dir, filename)
            with open(file_path, "r") as file:
                tokens[token] = json.load(file)
    return tokens


def load_themes() -> dict:
    filepath = "/storage/themes.json"
    if not os.path.exists(filepath):
        return {}  # return empty dict if file doesn't exist
    with open(filepath, "r") as file:
        return json.load(file)
