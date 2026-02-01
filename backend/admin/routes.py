import os
import shutil

from account.helpers import gen_user, get_user
from fastapi import APIRouter, Depends, HTTPException, status
from util.state import STATE, User
from util.tools import reserved_universe_names
from world.helpers import colors_to_image, world_colors

admin_router = APIRouter()


@admin_router.post("/state")
def state_route(user: User = Depends(get_user)) -> dict:
    if user.username != "Hunter":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username",
        )
    return {
        "tokens": STATE.auth_tokens,
        "users": STATE.users,
        "themes": STATE.themes,
        "cells": STATE.cells,
    }


@admin_router.post("/purge")
def pruge_route(user: User = Depends(get_user)) -> None:
    if not user.username != "Hunter":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username",
        )

    storage_path = "/storage"

    # Clear everything inside the folder but keep the folder itself
    for item in os.listdir(storage_path):
        item_path = os.path.join(storage_path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)  # remove file or symlink
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # remove directory and its contents

    # Make sure the storage folders exists
    os.makedirs("/storage/users", exist_ok=True)
    os.makedirs("/storage/cells", exist_ok=True)
    os.makedirs("/storage/tokens", exist_ok=True)

    for name in reserved_universe_names():
        STATE.users[name] = gen_user(name)
        STATE.themes[name] = ["#000000", "#FFFFFF"]

    # Set a default token for Hunter (Quick Developmnent)
    STATE.auth_tokens["Hunter"] = "asd"
    return


@admin_router.post("/make")
def make_route(size: int = 200, user: User = Depends(get_user)) -> None:
    if not user.username == "Hunter":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username",
        )

    colors = world_colors(size)
    buffer = colors_to_image(colors)
    STATE.image = buffer
    return
