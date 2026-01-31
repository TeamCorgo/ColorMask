import random

from util.state import STATE, Cell


def gen_cord(x: int, y: int, universe: str) -> str:
    return f"{str(x)}:{str(y)}:{universe}"


def gen_color(x: int, y: int, universe: str) -> None:
    rng = random.Random(STATE.seed + ":" + gen_cord(x, y, universe))
    cell = Cell(color=rng.choice(STATE.themes[universe]))
    STATE.worlds[gen_cord(x, y, universe)] = cell
    return
