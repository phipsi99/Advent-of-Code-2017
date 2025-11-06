


from tqdm import tqdm


def do_main(debug_mode=False):
    step = 337

    if debug_mode:
        step = 3

    spinlock = [0, 1]
    pointer = 1
    for i in range(2, 2018):
        pointer = ((pointer + step) % len(spinlock)) + 1
        spinlock.insert(pointer, i)
    res_idx = spinlock.index(2017) + 1
    print(spinlock[res_idx])

    spinlock_len = 2
    pointer = 1
    idx_0 = 0
    val = 0
    it = 50_000_000
    for i in tqdm(range(2, it)):
        pointer = ((pointer + step) % spinlock_len) + 1
        if pointer < idx_0:
            idx_0 += 1
        elif pointer == idx_0 + 1:
            val = i
        spinlock_len += 1
    print(val)


if __name__ == '__main__':
    do_main(False)