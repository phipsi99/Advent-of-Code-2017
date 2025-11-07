from pathlib import Path

import numpy as np
from tqdm import tqdm

def flatten(array):
    rule_as_str = np.array2string(array, separator='', max_line_width=np.inf, suppress_small=True)
    rule_as_str = rule_as_str.replace('[','').replace(']','').replace('\n','').replace(' ','').replace("'", "")
    return rule_as_str

def do_main(debug_mode=False):
    with open(Path('21/input.txt')) as file:
        lines = [line.rstrip() for line in file if line.strip()]

    if debug_mode:
        with open(Path('21/test.txt')) as file:
            lines = [line.rstrip() for line in file if line.strip()]

    point_sum = 0
    start_pattern = np.array([list(".#."), list("..#"), list("###")])

    rules = {}

    for line_index, line in enumerate(lines):
        # ../.# => ##./#../...
        r_left, r_right = line.split(" => ")
        r_left_parts = r_left.split("/")
        r_right_parts = r_right.split("/")
        right_pattern = np.array([list(x) for x in r_right_parts])
        pattern = np.array([list(x) for x in r_left_parts])
        pattern_flipped_vertically = np.fliplr(pattern)
        pattern_flipped_horizontally = np.flipud(pattern)
        for pat in [pattern, pattern_flipped_vertically, pattern_flipped_horizontally]:
            for rotations in range(4):
                new_pattern = np.rot90(pat, rotations)
                rules[flatten(new_pattern)] = right_pattern

    grid = np.copy(start_pattern)
    for h in tqdm(range(18)):
        size = len(grid)
        size_to_be = 2 if (size % 2 == 0) else 3
        new_grids = grid.reshape(int(size/size_to_be), size_to_be, int(size/size_to_be), size_to_be).swapaxes(1, 2)
        transformed_grids = np.empty((int(size/size_to_be), int(size/size_to_be), size_to_be+1, size_to_be+1), dtype=str)
        for i in range(new_grids.shape[0]):
            for j in range(new_grids.shape[1]):
                block = new_grids[i, j]
                transformed_grids[i, j] = rules[flatten(block)]
        n_blocks, _, block_size, _ = transformed_grids.shape
        grid = transformed_grids.swapaxes(1, 2).reshape(n_blocks*block_size, n_blocks*block_size)
        if h == 4:
            count = np.sum(grid == '#')
            print(count)
    count = np.sum(grid == '#')
    print(count)

if __name__ == '__main__':
    do_main(False)