from pathlib import Path
import numpy as np

def do_main(debug_mode=False):
    input = 312051
        
    ring_max = 1
    rings = 0
    ring_row = 1
    while ring_max < input:
        ring_max += ring_row*4 + 4
        ring_current = ring_row*4 + 4
        ring_row += 2
        rings += 1
    ring_first = ring_max-ring_current+1
    per_side = ring_row - 1
    while input > ring_first + per_side:
        input -= per_side
    index_input = input % ring_first
    best_index = rings - 1
    index_diff = abs(index_input-best_index)
    result = rings+index_diff 
    print(result)
    
    grid_size = 1000
    grid = np.zeros((grid_size, grid_size))
    grid[int(grid_size/2),int(grid_size/2)] = 1
    rings = 0
    num_per_side = 0
    index_row = int(grid_size/2)
    index_col = int(grid_size/2)
    while True:
        index_col += 1
        num_per_side += 2
        for i in range(num_per_side):
            if i > 0:
                index_row -= 1
            grid[index_row, index_col] = get_sum_of_adjectent(grid, index_row, index_col)
            if grid[index_row, index_col] > input:
                print(grid[index_row, index_col])
                return
        for i in range(num_per_side):
            index_col -= 1
            grid[index_row, index_col] = get_sum_of_adjectent(grid, index_row, index_col)
            if grid[index_row, index_col] > input:
                print(grid[index_row, index_col])
                return
        for i in range(num_per_side):
            index_row += 1
            grid[index_row, index_col] = get_sum_of_adjectent(grid, index_row, index_col)
            if grid[index_row, index_col] > input:
                print(grid[index_row, index_col])
                return
        for i in range(num_per_side):
            index_col += 1
            grid[index_row, index_col] = get_sum_of_adjectent(grid, index_row, index_col)
            if grid[index_row, index_col] > input:
                print(grid[index_row, index_col])
                return
        
        
    for row in grid:
        print(' '.join(f'{int(val)}' for val in row))
    
def get_sum_of_adjectent(grid, index_row, index_col):
    sum = 0
    for dir in [(-1,-1), (-1,0), (-1, 1), (0, 1), (1,1),(1,0),(1,-1),(0,-1)]:
        sum+=grid[index_row+dir[0],index_col+dir[1]]
    return sum

if __name__ == '__main__':
    do_main(False)