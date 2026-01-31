from account.helpers import gen_user
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from util.state import STATE
from util.tools import reserved_universe_names

scheduler = AsyncIOScheduler()


async def recurring_task():
    print("⚙️ Running task")
    print("🛑 Task finished")


def startup() -> None:
    print("⚙️ Startup")
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
    print(STATE.users)
    scheduler.shutdown()
    print("🛑 Shutdown finished")
    return
