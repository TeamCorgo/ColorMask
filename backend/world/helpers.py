import random

from PIL import Image
from util.state import STATE, User


def gen_cord(x: str, y: str, universe: str) -> str:
    return f"{x}:{y}:{universe}"


def gen_color(x: int, y: int, universe: str) -> str:
    cord = gen_cord(x, y, universe)
    rng = random.Random(STATE.seed + ":" + cord)
    return rng.choice(STATE.themes[universe])


def world_view(x: int, y: int, universe: str, size: int) -> list:
    view = []
    for row in range(size):  # top → bottom (y)
        for col in range(size):  # left → right (x)
            cord = gen_cord(str(x + col), str(y + row), universe)
            synthetic_color = ""
            if cord in STATE.cells:
                synthetic_color = STATE.cells[cord]
            # check if cell doesnt exists in world
            if cord not in STATE.cells:
                # Generate the cell
                synthetic_color = gen_color(x + col, y + row, universe)
                STATE.cells[cord] = synthetic_color
            # read the cell from world
            view.append(synthetic_color)

    return view


def player_view(user: User) -> list:
    size = 5
    # Offset the starting coordinates so the player is centered
    start_x = user.x - size // 2
    start_y = user.y - size // 2
    return world_view(start_x, start_y, user.universe, 5)


def tron_check(user: User, x: int, y: int) -> bool:
    cord = gen_cord(x, y, user.universe)
    if cord not in STATE.cells:
        # This cell has never been player set
        return False
    cell_color = STATE.cells[cord]

    # Black cannot walk onto White
    if user.color == "#000000" and cell_color == "#FFFFFF":
        return True

    # White cannot walk onto Black
    if user.color == "#FFFFFF" and cell_color == "#000000":
        return True

    # Red cannot walk onto Green
    if user.color == "#FF0000" and cell_color == "#00FF00":
        return True

    # Green cannot walk onto Red
    if user.color == "#00FF00" and cell_color == "#FF0000":
        return True

    # Blue cannot walk onto Orange
    if user.color == "#0000FF" and cell_color == "#FFA500":
        return True

    # Orange cannot walk onto Blue
    if user.color == "#FFA500" and cell_color == "#0000FF":
        return True

    # Yellow cannot walk onto Purple
    if user.color == "#FFFF00" and cell_color == "#800080":
        return True

    # Purple cannot walk onto Yellow
    if user.color == "#800080" and cell_color == "#00FF00":
        return True
    return False


def world_image(size: int) -> list:
    colors = world_view(0 - int(size / 2), 0 - int(size / 2), "0", size)
    print(colors)

    grid_size = size
    cell_size = 1  # pixels per square

    img_size = grid_size * cell_size
    img = Image.new("RGB", (img_size, img_size))

    for i, color in enumerate(colors):
        x = (i % grid_size) * cell_size
        y = (i // grid_size) * cell_size

        for px in range(x, x + cell_size):
            for py in range(y, y + cell_size):
                img.putpixel(
                    (px, py), tuple(int(color[j : j + 2], 16) for j in (1, 3, 5))
                )

    # img.save("grid.png")

    return colors
