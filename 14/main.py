
from collections import deque
import numpy as np
from utils.utils import CircularList

def knot_hash(input_str):
    lengths = [ord(i) for i in input_str]
    lengths.extend([17, 31, 73, 47, 23])
    circle = CircularList(list(range(256)))
    pointer = 0
    skip_size = 0
    for i in range(64):
        for length in lengths:
            start_index = pointer
            end_index = pointer + length
            circle[start_index:end_index] = circle[start_index:end_index][::-1]
            pointer = (pointer + length + skip_size) % len(circle)
            skip_size += 1
    dense_hash = []
    for j in range(16):
        dense_char = circle[j*16]
        for k in range(1, 16):
            dense_char = dense_char ^ circle[j*16+k]
        dense_hash.append(dense_char)
    return ''.join(f"{x:02x}" for x in dense_hash)

def do_main(debug_mode=False):
    key = "vbqugkhl"

    if debug_mode:
        key = "flqrgnkx"

    count = 0

    grid = np.empty((128, 128), dtype=str)

    for i in range(128):
        hash_input = f"{key}-{i}"
        hashed_key = knot_hash(hash_input)
        binary_value = bin(int(hashed_key, 16))[2:].zfill(len(hashed_key) * 4)
        count += binary_value.count('1')
        grid[i, :] = list(binary_value.replace("1", "#").replace("0", "."))
    print(count)

    groups = 0
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]
    for i in range(128):
        for j in range(128):
            if grid[i, j] != "#":
                continue
            groups += 1
            queue = deque([(i, j)])
            while queue:
                elem = queue.popleft()
                grid[elem[0], elem[1]] = groups
                for dir in directions:
                    new_row = elem[0]+dir[0]
                    new_col =  elem[1]+dir[1]
                    if new_row < 0 or new_col < 0 or new_row > 127 or new_col > 127:
                        continue
                    adjectent = grid[new_row, new_col]
                    if adjectent == "#":
                        queue.append((new_row, new_col))
    print(groups)


if __name__ == '__main__':
    do_main(False)