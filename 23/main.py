from pathlib import Path
import re


def do_main(debug_mode=False):
    with open(Path("23/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("23/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    instructions = []
    registers = {}

    for c in range(ord("a"), ord("i")):
        registers[chr(c)] = 0

    for line_index, line in enumerate(lines):
        op, a, b = line.split(" ")
        try:
            a = int(a)
        except:
            pass
        try:
            b = int(b)
        except:
            pass
        instructions.append((op, a, b))

    pointer = 0
    while pointer < len(instructions):
        op, a, b = instructions[pointer]
        if not isinstance(b, int):
            b = registers[b]
        if op == "set":
            registers[a] = b
        elif op == "sub":
            registers[a] -= b
        elif op == "mul":
            registers[a] *= b
            point_sum += 1
        elif op == "jnz":
            if not isinstance(a, int):
                a = registers[a]
            if a != 0:
                pointer += b - 1
        pointer += 1
    print(point_sum)

    point_sum2 = 0
    for num in range(106_700, 106_700 + 17000, 17):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if not prime:
            point_sum2 += 1

    print(point_sum2 + 1)


if __name__ == "__main__":
    do_main(False)
