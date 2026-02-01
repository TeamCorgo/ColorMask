import os

from account.helpers import gen_user
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from util.state import STATE
from util.tools import cells_to_json, reserved_universe_names, users_to_json

scheduler = AsyncIOScheduler()


async def recurring_task():
    print("⚙️ Running task")

    users_to_json(STATE.users)
    print("Total users stored:", len(STATE.users))
    cells_to_json(STATE.cells)
    print("Total cells stored:", len(STATE.cells))
    print("🛑 Task finished")


def startup() -> None:
    print("⚙️ Startup")

    # Make sure the storage folders exists
    os.makedirs("/storage/users", exist_ok=True)
    os.makedirs("/storage/cells", exist_ok=True)

    # Create an account for each system "user"
    for name in reserved_universe_names():
        STATE.users[name] = gen_user(name)
        STATE.themes[name] = ["#000000", "#FFFFFF"]

    # Set a default token for Hunter (Quick Developmnent)
    STATE.auth_tokens["Hunter"] = "asd"

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
