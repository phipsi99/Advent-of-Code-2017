from pathlib import Path

from tqdm import tqdm

from utils.direction_simple import DirectionSimple
from utils.infinite_grid import InfiniteGrid


def do_main(debug_mode=False):
    with open(Path("22/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("22/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    grid = InfiniteGrid(dtype=str, empty_value=".")
    grid.load_from_string(
        lines,
        origin=(
            -int(len(lines[0]) / 2),
            -int(len(lines[0]) / 2),
        ),  # , mapping={".":False, "#": True}
    )
    carrier_pos_x = 0
    carrier_pos_y = 0
    carrier_dir = DirectionSimple.UP
    for i in tqdm(range(10000)):
        if grid.get(carrier_pos_x, carrier_pos_y) == ".":
            carrier_dir = carrier_dir.left()
            grid.set(carrier_pos_x, carrier_pos_y, "#")
            carrier_pos_x += carrier_dir.dx
            carrier_pos_y += carrier_dir.dy
            point_sum += 1
        else:
            carrier_dir = carrier_dir.right()
            grid.set(carrier_pos_x, carrier_pos_y, ".")
            carrier_pos_x += carrier_dir.dx
            carrier_pos_y += carrier_dir.dy
    print(grid.region_to_string(-10, -10, 20, 20))
    print(point_sum)
    
    point_sum2 = 0
    grid = InfiniteGrid(dtype=str, empty_value=".")
    grid.load_from_string(
        lines,
        origin=(
            -int(len(lines[0]) / 2),
            -int(len(lines[0]) / 2),
        ),  # , mapping={".":False, "#": True}
    )
    carrier_pos_x = 0
    carrier_pos_y = 0
    carrier_dir = DirectionSimple.UP
    for i in tqdm(range(10000000)):
        if grid.get(carrier_pos_x, carrier_pos_y) == ".":
            carrier_dir = carrier_dir.left()
            grid.set(carrier_pos_x, carrier_pos_y, "W")
            carrier_pos_x += carrier_dir.dx
            carrier_pos_y += carrier_dir.dy
        elif grid.get(carrier_pos_x, carrier_pos_y) == "W":
            grid.set(carrier_pos_x, carrier_pos_y, "#")
            carrier_pos_x += carrier_dir.dx
            carrier_pos_y += carrier_dir.dy
            point_sum2 += 1
        elif grid.get(carrier_pos_x, carrier_pos_y) == "#":
            carrier_dir = carrier_dir.right()
            grid.set(carrier_pos_x, carrier_pos_y, "F")
            carrier_pos_x += carrier_dir.dx
            carrier_pos_y += carrier_dir.dy
        elif grid.get(carrier_pos_x, carrier_pos_y) == "F":
            carrier_dir = carrier_dir.right().right()
            grid.set(carrier_pos_x, carrier_pos_y, ".")
            carrier_pos_x += carrier_dir.dx
            carrier_pos_y += carrier_dir.dy
    print(grid.region_to_string(-10, -10, 20, 20))
    print(point_sum2)


if __name__ == "__main__":
    do_main(False)
