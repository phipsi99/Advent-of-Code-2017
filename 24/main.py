from collections import deque
import copy
from pathlib import Path

from tqdm import tqdm


def do_main(debug_mode=False):
    with open(Path("24/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("24/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    components = []

    for line_index, line in enumerate(lines):
        components.append([int(i) for i in line.split("/")])

    start_components = []

    for c in components:
        if c[0] == 0:
            start_components.append(c)

    queue = deque([])
    for c in start_components:
        queue.append([c])

    strongest = 0
    longest = [[]]
    pbar = tqdm(total=0, position=0, dynamic_ncols=True)
    processed = 0

    while queue:
        used_components = queue.popleft()
        last_component = used_components[-1]
        processed += 1
        pbar.update(1)
        pbar.set_description(f"Queue={len(queue)} | Processed={processed}")
        found_new = False
        for c in components:
            if c in used_components or c[::-1] in used_components:
                continue
            if last_component[1] not in c:
                continue
            new_components = used_components[:]
            new_components.append(c if last_component[1] == c[0] else c[::-1])
            queue.append(new_components)
            found_new = True
        if not found_new:
            if any(len(used_components) > len(l) for l in longest):
                longest = [used_components]
            elif len(used_components) == len(longest[0]):
                longest.append(used_components)
            strength = sum(sum(c) for c in used_components)
            strongest = max(strongest, strength)

    pbar.close()
    print(strongest)
    strongest_longest = max(sum(sum(c) for c in l) for l in longest)
    print(strongest_longest)


if __name__ == "__main__":
    do_main(False)
