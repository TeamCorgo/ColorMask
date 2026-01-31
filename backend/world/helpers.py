import random

from util.state import STATE, Cell, User


def gen_cord(x: str, y: str, universe: str) -> str:
    return f"{x}:{y}:{universe}"


def gen_color(x: int, y: int, universe: str) -> str:
    rng = random.Random(STATE.seed + ":" + gen_cord(x, y, universe))
    cell = Cell(color=rng.choice(STATE.themes[universe]))
    STATE.cells[gen_cord(x, y, universe)] = cell
    return cell.color


def world_view(x: int, y: int, universe: str, size: int) -> list:
    view = []
    for row in range(size):  # top → bottom (y)
        for col in range(size):  # left → right (x)
            cord = gen_cord(str(x + col), str(y + row), universe)
            # check if cell doesnt exists in world
            if cord not in STATE.cells:
                # Generate the cell
                STATE.cells[cord] = gen_color(x + col, y + row, universe)
            # read the cell from world
            view.append(STATE.cells[cord])

    return view


def player_view(user: User) -> list:
    size = 5
    # Offset the starting coordinates so the player is centered
    start_x = user.x - size // 2
    start_y = user.y - size // 2
    return world_view(start_x, start_y, user.universe, 5)
