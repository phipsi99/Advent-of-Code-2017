from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('06/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('06/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    states = []

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(" ")]
        while True:
            idx_max = r.index(max(r))
            indices_to_add_to = range(idx_max + 1, idx_max + 1 + r[idx_max]) 
            cleaned_idx_to_add_to = [x % len(r) for x in indices_to_add_to]
            r[idx_max] = 0
            for i in cleaned_idx_to_add_to:
                r[i] += 1 
            point_sum += 1
            if r in states:
                break
            states.append(r.copy())
    
    print(point_sum)
    print(point_sum - (states.index(r) + 1))
        

if __name__ == '__main__':
    do_main(False)