from collections import deque
from pathlib import Path
import re

import numpy as np

def do_main(debug_mode=False):
    with open(Path('19/input.txt')) as file:
        lines = [line.replace("\n", "") for line in file]

    if debug_mode:
        with open(Path('19/test.txt')) as file:
            lines = [line.replace("\n", "")for line in file]

    point_sum = 0
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len, " ") for line in lines]
    grid = np.array([list(line) for line in lines])

    start = int(np.where(grid[0] == '|')[0][0])
    queue = deque([(0, start, "down", False)])
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
        }
    opposite_dir_map = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    path = [(0, start)]
    letters = []

    while queue:
        row, col, direction, found_crossing = queue.popleft()
        if not found_crossing:
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]
            if 0 > new_row or new_row >= len(grid) or 0 > new_col or new_col >= len(grid[0]):
                continue
            if re.match(r"[A-Z]", grid[new_row, new_col]):
                letters.append(grid[new_row, new_col])
            elif grid[new_row, new_col] == ' ':
                break
            elif grid[new_row, new_col] == '+':
                queue.append((new_row, new_col, direction, True))
                path.append((new_row, new_col))
                continue
            queue.append((new_row, new_col, direction, False))
            path.append((new_row, new_col))
        else:
            for key, (dir_row, dir_col) in directions.items():
                new_row = row + dir_row
                new_col = col + dir_col
                if 0 > new_row or new_row >= len(grid) or 0 > new_col or new_col >= len(grid[0]):
                    continue
                if direction == key or opposite_dir_map[direction] == key or grid[new_row, new_col] == " ":
                    continue
                if re.match(r"[A-Z]", grid[new_row, new_col]):
                    letters.append(grid[new_row, new_col])
                elif grid[new_row, new_col] == '+':
                    queue.append((new_row, new_col, key, True))
                    path.append((new_row, new_col))
                    continue
                queue.append((new_row, new_col, key, False))
                path.append((new_row, new_col))

    print("".join(letters))
    print(len(path))


if __name__ == '__main__':
    do_main(False)