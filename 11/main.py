from pathlib import Path

import numpy as np

def do_main(debug_mode=False):
    with open(Path('11/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('11/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    path = lines[0].split(",")

    directions = {
        "n": (1, 0, -1),
        "nw": (1, -1, 0),
        "ne": (0, +1, -1),
        "sw": (0, -1, +1),
        "se": (-1, +1, 0),
        "s": (-1, 0, +1),
    }
    max_distance = 0
    field = np.array([0,0,0])
    for step in path:
        direction = directions[step]
        field += direction
        max_distance = max(np.max(np.abs(field)), max_distance)
    distance = np.max(np.abs(field))
    print(distance)
    print(max_distance)


if __name__ == '__main__':
    do_main(False)