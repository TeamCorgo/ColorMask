from account.helpers import get_user
from fastapi import APIRouter, Depends
from util.state import STATE, User
from world.helpers import gen_cord, player_view

game_router = APIRouter()


@game_router.post("/view")
def view_route(user: User = Depends(get_user)) -> dict:
    userdata = {
        "username": user.username,
        "posx": user.x,
        "posy": user.y,
        "universe": user.universe,
        "color": user.color,
    }
    return {"view": player_view(user), "userdata": userdata}


@game_router.post("/move_north")
def move_north(user: User = Depends(get_user)) -> dict:
    user.y -= 1
    return {"message": "Moved north", "view": player_view(user)}


@game_router.post("/move_south")
def move_south(user: User = Depends(get_user)) -> dict:
    user.y += 1
    return {"message": "Moved south", "view": player_view(user)}


@game_router.post("/move_east")
def move_east(user: User = Depends(get_user)) -> dict:
    user.x += 1
    return {"message": "Moved east", "view": player_view(user)}


@game_router.post("/move_west")
def move_west(user: User = Depends(get_user)) -> dict:
    user.x -= 1
    return {"message": "Moved west", "view": player_view(user)}


@game_router.post("/paint")
def paint(user: User = Depends(get_user)) -> None:
    cord = gen_cord(user.x, user.y, user.universe)
    # cell = Cell(color=rng.choice(STATE.themes[user.universe]))
    # STATE.cells[cord] = cell
    STATE.cells[cord] = user.color
    # return {"message": "Moved west", "view": player_view(user)}
    return {"message": "Paint", "view": player_view(user)}
