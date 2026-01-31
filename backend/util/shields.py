import re


def shield_username(username: str) -> bool:
    regex = re.compile(r"^[A-Za-z0-9]{1,16}$")
    return regex.match(username)
