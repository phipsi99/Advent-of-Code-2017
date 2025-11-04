import copy
from pathlib import Path

import numpy as np


def simulate_firewall(scanner_indexes, ranges, wait):
    scanner_indexes_local = copy.deepcopy(scanner_indexes)
    scanner_indexes_local += wait
    caught = []
    for i, (scanner_index, scanner_range) in enumerate(zip(scanner_indexes_local, ranges)):
        if (not np.isnan(scanner_index)) and int(scanner_index) % ((int(scanner_range)-1) *2) == 0:
            caught.append(i)
        scanner_indexes_local += 1
    return caught
        
        

def do_main(debug_mode=False):
    with open(Path('13/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('13/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    
    highest = int(lines[-1].split(": ")[0])
    point_sum = 0
    scanner_indexes = np.full(highest+1, np.nan)
    ranges =  np.full(highest+1, np.nan)

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(": ")]
        scanner_indexes[r[0]] = 0
        ranges[r[0]] = r[1]
        
        
    caught = simulate_firewall(scanner_indexes, ranges, 0)
    print(caught)
    print(sum(i * ranges[i] for i in caught))
    
    wait = 0
    while True:
        caught = simulate_firewall(scanner_indexes, ranges, wait)
        if len(caught) == 0:
            print(wait)
            break
        if wait % 1000 == 0:
            print(wait)
        wait += 1
    

if __name__ == '__main__':
    do_main(False)