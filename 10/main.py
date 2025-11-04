from pathlib import Path
class CircularList(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self) * 2)
            return [self[i % len(self)] for i in range(start, stop, step)]
        return super().__getitem__(index % len(self))

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self) * 2)
            for i, val in zip(range(start, stop, step), value):
                super().__setitem__(i % len(self), val)
        else:
            super().__setitem__(index % len(self), value)


def do_main(debug_mode=False):
    with open(Path('10/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('10/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    lenghts = [int(i) for i in lines[0].split(",")]
    circle = CircularList(list(range(256)))
    pointer = 0
    skip_size = 0
    for length in lenghts:
        start_index = pointer
        end_index = pointer + length
        circle[start_index:end_index] = circle[start_index:end_index][::-1]
        pointer = (pointer + length + skip_size) % len(circle)
        skip_size += 1
    print(circle[0]*circle[1])

    lenghts = [ord(i) for i in lines[0]]
    lenghts.extend([17, 31, 73, 47, 23])
    circle = CircularList(list(range(256)))
    pointer = 0
    skip_size = 0
    for i in range(64):
        for length in lenghts:
            start_index = pointer
            end_index = pointer + length
            circle[start_index:end_index] = circle[start_index:end_index][::-1]
            pointer = (pointer + length + skip_size) % len(circle)
            skip_size += 1
    dense_hash = []
    for j in range(16):
        dense_char = circle[j*16]
        for k in range(1, 16):
            dense_char = dense_char ^ circle[j*16+k]
        dense_hash.append(dense_char)
    print(''.join(f"{x:02x}" for x in dense_hash))

if __name__ == '__main__':
    do_main(False)