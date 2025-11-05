from pathlib import Path
import re

from tqdm import tqdm

def dance(dancers, moves):
    for move in moves:
        if move.startswith("s"):
            size = int(re.findall(r"\d+", move)[0])
            dancers = dancers[-size:] + dancers[:len(dancers)-size]
        elif move.startswith("x"):
            indexes = [int(i) for i in re.findall(r"\d+", move)]
            old = dancers[indexes[0]]
            dancers[indexes[0]] = dancers[indexes[1]]
            dancers[indexes[1]] = old
        elif move.startswith("p"):
            partners = re.findall(r"[a-z]", move[1:])
            index_a = dancers.index(partners[0])
            index_b = dancers.index(partners[1])
            dancers[index_a] = partners[1]
            dancers[index_b] = partners[0]
    return dancers

def do_main(debug_mode=False):
    with open(Path('16/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    dancers = [chr(c) for c in range(ord('a'), ord('q'))]

    if debug_mode:
        with open(Path('16/test.txt')) as file:
            lines = [line.rstrip() for line in file]
        dancers = [chr(c) for c in range(ord('a'), ord('f'))]

    point_sum = 0

    moves = lines[0].split(',')
    part1 = dance(dancers, moves)
    print(''.join(part1))

    for i in tqdm(range(1000000000)):
        dancers = dance(dancers, moves)
    print(''.join(dancers))

if __name__ == '__main__':
    do_main(False)