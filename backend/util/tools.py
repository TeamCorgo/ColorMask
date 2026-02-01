import json


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


def users_to_json(users: dict):
    for username, user in users.items():
        file_path = f"/storage/users/{username}.json"
        with open(file_path, "w") as file:
            json.dump(user, file, default=vars, indent=4)
    return


def cells_to_json(cells: dict):
    for cord, cell in cells.items():
        file_path = f"/storage/cells/{cord}.json"

        with open(file_path, "w") as file:
            json.dump(cell, file, default=vars, indent=4)
    return