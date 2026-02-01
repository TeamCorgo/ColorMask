import os

from account.helpers import gen_user
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from util.state import STATE
from util.tools import (
    reserved_universe_names,
)

scheduler = AsyncIOScheduler()


async def recurring_task() -> None:
    print("⚙️ Running task")
    print("🛑 Task finished")
    return


def startup() -> None:
    print("⚙️ Startup")

    # Make sure the storage folders exists
    os.makedirs("/storage/users", exist_ok=True)
    os.makedirs("/storage/cells", exist_ok=True)
    os.makedirs("/storage/tokens", exist_ok=True)

    # Database Hydration script
    # Create an account for each system "user"
    # print(reserved_universe_names())
    for name in reserved_universe_names():
        STATE.users[name] = gen_user(name)
        # STATE.themes[name] = ["#000000", "#FFFFFF"]
        STATE.themes[name] = [
            "#f2b3b0",
            "#ffe08b",
            "#aad4ff",
            "#9ee0b9",
            "#f0c1f0",
            "#ffb8a3",
            "#b0c6ff",
            "#ffdca3",
            "#c4f0a8",
            "#a0e0ff",
            "#f4d1c7",
            "#d4baff",
            "#c0fff0",
            "#ffcae0",
            "#e0ffb0",
        ]

    # Set a default token for Hunter (Quick Developmnent)
    STATE.auth_tokens["Hunter"] = "asd"
    STATE.cells["0:0:0"] = "#FF69B4"

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
