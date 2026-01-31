import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from util.state import STATE, User


# Generate a random token
def generate_auth_token() -> str:
    return secrets.token_hex(16)  # 32-character hex token


# Validate token and return the spesific user
def get_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> User:
    access_token = credentials.credentials

    # Find the username that matches the provided token
    username = next(
        (user for user, token in STATE.auth_tokens.items() if token == access_token),
        None,
    )

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return STATE.users[username]


def gen_user(username: str) -> User:
    STATE.auth_tokens[username] = generate_auth_token()
    return User(username=username)
