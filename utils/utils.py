import numpy as np
from collections import defaultdict


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

    def insert(self, index, value):
        if self:
            index = index % len(self)
        else:
            index = 0
        super().insert(index, value)


def grid_from_lines(lines, mapping=None, dtype=str):
    h = len(lines)
    w = len(lines[0]) if h > 0 else 0

    grid = np.empty((h, w), dtype=dtype)

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            grid[y, x] = mapping[ch] if mapping else ch
    return grid


def lines_from_grid(grid, reverse_mapping=None):
    h, w = grid.shape
    lines = []

    for y in range(h):
        row = []
        for x in range(w):
            val = grid[y, x]
            if reverse_mapping:
                val = reverse_mapping.get(val, "?")
            row.append(str(val))
        lines.append("".join(row))
    return lines

