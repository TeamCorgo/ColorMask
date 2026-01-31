from account.helpers import gen_user, generate_auth_token, get_user
from account.models import RegisterModel
from fastapi import APIRouter, Depends, HTTPException, status
from util.shields import shield_username
from util.state import STATE, User

account_router = APIRouter()


@account_router.get("/protected")
def protected_route(user: User = Depends(get_user)) -> dict:
    return {
        "message": f"This is a protected route for the user: {user.username}.",
    }


@account_router.post("/regenerate")
def regenerate(user: User = Depends(get_user)) -> dict:
    STATE.auth_tokens[user.username] = generate_auth_token()
    return {"token": STATE.auth_tokens[user.username]}


# Registration route
@account_router.post("/register")
def register(recieve: RegisterModel) -> dict:
    # Username must be A-Z, a-z, 0-9 (limit to 16 chars)
    if not shield_username(recieve.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username. Only A-Z, a-z, 0-9 allowed, max 16 chars.",
        )

    # Cannot be a reserved name
    if recieve.username == "0":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username. Reserved name.",
        )

    # Cannot be already registered
    if recieve.username in STATE.users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    STATE.users[recieve.username] = gen_user(recieve.username)
    return {"token": STATE.auth_tokens[recieve.username]}
