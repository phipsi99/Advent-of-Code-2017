from pathlib import Path

import numpy as np
from numba import njit

@njit
def test_speed(offsets):
    pointer = 0
    point_sum = 0
    while pointer < len(offsets):
        old_pointer = pointer
        pointer += offsets[pointer]
        if offsets[old_pointer] >= 3:
            offsets[old_pointer] -= 1
        else:
            offsets[old_pointer] += 1
        point_sum += 1
    return point_sum


def do_main(debug_mode=False):
    with open(Path('05/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('05/test.txt')) as file:
            lines = [line.rstrip() for line in file]
            
    point_sum = 0
    offsets = []

    for line_index, line in enumerate(lines):
        offsets.append(int(line))
    
    pointer = 0
    while pointer < len(offsets):
        old_pointer = pointer
        pointer += offsets[pointer]
        offsets[old_pointer] += 1
        point_sum += 1
    
    print(point_sum)

    point_sum = 0
    offsets = []

    for line_index, line in enumerate(lines):
        offsets.append(int(line))
    
    print(test_speed(offsets))
    
    # pointer = 0
    # while pointer < len(offsets):
    #     old_pointer = pointer
    #     pointer += offsets[pointer]
    #     if offsets[old_pointer] >= 3:
    #         offsets[old_pointer] -= 1
    #     else:
    #         offsets[old_pointer] += 1
    #     point_sum += 1
    
    # print(point_sum)
        

if __name__ == '__main__':
    do_main(False)