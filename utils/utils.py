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