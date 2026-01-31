from account.helpers import get_user
from fastapi import APIRouter, Depends
from util.state import User
from world.helpers import player_view

game_router = APIRouter()


@game_router.post("/view")
def view_route(user: User = Depends(get_user)) -> dict:
    return {"view": player_view(user)}


@game_router.post("/move_north")
def move_north(user: User = Depends(get_user)) -> dict:
    user.y += 1
    return {"message": "Moved north", "view": player_view(user)}


@game_router.post("/move_south")
def move_south(user: User = Depends(get_user)) -> dict:
    user.y -= 1
    return {"message": "Moved south", "view": player_view(user)}


@game_router.post("/move_east")
def move_east(user: User = Depends(get_user)) -> dict:
    user.x += 1
    return {"message": "Moved east", "view": player_view(user)}


@game_router.post("/move_west")
def move_west(user: User = Depends(get_user)) -> dict:
    user.x -= 1
    return {"message": "Moved west", "view": player_view(user)}
