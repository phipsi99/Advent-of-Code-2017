


from tqdm import tqdm


def do_main(debug_mode=False):
    gen_a_start = 277
    gen_b_start = 349

    if debug_mode:
        gen_a_start = 65
        gen_b_start = 8921

    point_sum = 0
    gen_a_factor = 16807
    gen_b_factor = 48271
    divisor = 2147483647
    mask = (1 << 16) - 1

    a_val = gen_a_start
    b_val = gen_b_start

    for i in tqdm(range(40000000)):
        a_val = (a_val * gen_a_factor) % divisor
        b_val = (b_val * gen_b_factor) % divisor
        if (a_val & mask) == (b_val & mask):
            point_sum += 1

    point_sum2 = 0
    a_val = gen_a_start
    b_val = gen_b_start
    a_vals = []
    b_vals = []
    while len(a_vals) < 5000000:
        a_val = (a_val * gen_a_factor) % divisor
        if a_val % 4 == 0:
            a_vals.append(a_val & mask)
    print("a vals done")
    while len(b_vals) < 5000000:
        b_val = (b_val * gen_b_factor) % divisor
        if b_val % 8 == 0:
            b_vals.append(b_val & mask)
    print("b vals done")

    for a, b in zip(a_vals, b_vals):
        if a == b:
            point_sum2 += 1

    print(point_sum)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)