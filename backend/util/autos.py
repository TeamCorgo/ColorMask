import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from util.state import STATE
from util.tools import (
    load_cells,
    load_themes,
    load_tokens,
    load_users,
    save_cells,
    save_themes,
    save_tokens,
    save_users,
)

scheduler = AsyncIOScheduler()


async def recurring_task() -> None:
    print("⚙️ Running task")

    save_users(STATE.users)
    print("Total users stored:", len(STATE.users))
    save_cells(STATE.cells)
    print("Total cells stored:", len(STATE.cells))
    save_tokens(STATE.auth_tokens)
    print("Total tokens stored:", len(STATE.auth_tokens))
    save_themes(STATE.themes)
    print("Total themes stored:", len(STATE.themes))
    print("🛑 Task finished")
    return


def startup() -> None:
    print("⚙️ Startup")

    # Make sure the storage folders exists
    os.makedirs("/storage/users", exist_ok=True)
    os.makedirs("/storage/cells", exist_ok=True)
    os.makedirs("/storage/tokens", exist_ok=True)

    # Read HDD into RAM
    STATE.users = load_users()
    STATE.auth_tokens = load_tokens()
    STATE.cells = load_cells()
    STATE.themes = load_themes()

    # Database Hydration script
    # Create an account for each system "user"
    # for name in reserved_universe_names():
    #    STATE.users[name] = gen_user(name)
    #    STATE.themes[name] = ["#000000", "#FFFFFF"]

    # Set a default token for Hunter (Quick Developmnent)
    # STATE.auth_tokens["Hunter"] = "asd"

    # print(STATE.users)
    # print(STATE.auth_tokens)
    # print(STATE.themes)
    scheduler.add_job(recurring_task, "interval", minutes=1)
    scheduler.start()
    print("🛑 Startup finished")
    return


def shutdown() -> None:
    print("⚙️ Shutdown")
    scheduler.shutdown()
    print("🛑 Shutdown finished")
    return
