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
    grid = np.array([list(line) for line in lines])
    
    start = np.where(grid[0] == '|')
    queue = deque([(0, start, True)])
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]
    path = set()
    letters = []
    
    while queue:
        row, col, vertical = queue.popleft()
        if vertical:
            directions = [(0,1), (0, -1)]
        else:
            directions = [(1,0), (-1, 0)]
        for dir in directions:
            new_row = row + dir[0]
            new_col = row + dir[1]
            if 0 > new_row > len(grid) or 0 > new_col > len(grid[0]):
                continue
            elif (new_row, new_col) in path:
                continue
            elif re.match(r"[A-Z]", grid[new_row, new_col]):
                letters.append(grid[new_row, new_col])
            elif grid[new_row, new_col] == '+':
                queue.append((new_row, new_col, not vertical))
            else:
                queue.append((new_row, new_col, vertical))
            

if __name__ == '__main__':
    do_main(True)