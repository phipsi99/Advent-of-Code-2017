from pathlib import Path

import numpy as np
from tqdm import tqdm


def do_main(debug_mode=False):

    steps = 12667664

    if debug_mode:
        steps = 6

    point_sum = 0
    pointer = int(steps / 2)

    turing = np.zeros(shape=(steps * 2 + 1,), dtype=bool)

    state = "A"

    for i in tqdm(range(6)):
        match state:
            case "A":
                old = turing[pointer]
                turing[pointer] = not old
                pointer += -1 if old else 1
                state = "B"
            case "B":
                old = turing[pointer]
                turing[pointer] = True
                pointer += 1 if old else -1
                state = "A"
        print("".join("1" if x else "0" for x in turing))

    print(np.count_nonzero(turing))


if __name__ == "__main__":
    do_main(True)
