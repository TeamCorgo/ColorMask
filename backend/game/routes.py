from account.helpers import get_user
from fastapi import APIRouter, Depends
from util.state import User
from world.helpers import player_view

game_router = APIRouter()


@game_router.post("/map")
def map_route(user: User = Depends(get_user)) -> dict:
    return {"map": player_view(user)}
