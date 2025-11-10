from collections import defaultdict
import numpy as np


class InfiniteArray:
    def __init__(self, ndim=2, chunk_size=32, dtype=np.int8, empty_value=0):
        """
        Generic N-dimensional infinite array made of chunked NumPy arrays.

        Args:
            ndim: number of dimensions (e.g., 2 for 2D, 3 for 3D)
            chunk_size: int or tuple of chunk sizes per dimension
            dtype: NumPy dtype for each chunk
            empty_value: value to fill new chunks with
        """
        self.ndim = ndim
        if isinstance(chunk_size, int):
            self.chunk_size = (chunk_size,) * ndim
        else:
            assert len(chunk_size) == ndim
            self.chunk_size = tuple(chunk_size)

        self.dtype = dtype
        self.empty_value = empty_value
        self.chunks = defaultdict(self._make_chunk)

    def _make_chunk(self):
        """Create a new chunk initialized to the empty_value."""
        return np.full(self.chunk_size, self.empty_value, dtype=self.dtype)

    def _chunk_coords(self, *coords):
        """
        Compute chunk and local coordinates for N dimensions.
        Handles negative indices properly.
        """
        chunk_coords = []
        local_coords = []
        for c, size in zip(coords, self.chunk_size):
            if c >= 0:
                cc = c // size
            else:
                cc = -((-c - 1) // size) - 1
            lc = c - cc * size
            chunk_coords.append(cc)
            local_coords.append(lc)
        return tuple(chunk_coords), tuple(local_coords)

    def get(self, *coords):
        chunk_coords, local_coords = self._chunk_coords(*coords)
        return self.chunks[chunk_coords][local_coords]

    def set(self, *coords, value):
        chunk_coords, local_coords = self._chunk_coords(*coords)
        self.chunks[chunk_coords][local_coords] = value

    def region(self, starts, sizes):
        """
        Extract a rectangular/slice region as a NumPy array.
        Args:
            starts: tuple of start indices (inclusive)
            sizes: tuple of extents (number of elements per axis)
        Returns:
            NumPy array containing the region.
        """
        assert len(starts) == self.ndim == len(sizes)
        result = np.empty(sizes, dtype=self.dtype)
        it = np.ndindex(*sizes)
        for offset in it:
            coords = tuple(s + o for s, o in zip(starts, offset))
            result[offset] = self.get(*coords)
        return result

    def fill_region(self, starts, data):
        """
        Write data (NumPy array) into region starting at `starts`.
        """
        it = np.ndindex(*data.shape)
        for offset in it:
            coords = tuple(s + o for s, o in zip(starts, offset))
            self.set(*coords, value=data[offset])

    def region_to_string(self, x0, y0, w, h, mapping=None):
        """
        Convenience 2D visualizer for 2D arrays.
        """
        if self.ndim != 2:
            raise ValueError("region_to_string only works for 2D arrays")
        if mapping is None:
            mapping = {}
        out = []
        for y in range(y0, y0 + h):
            row = ""
            for x in range(x0, x0 + w):
                val = self.get(x, y)
                row += mapping.get(val, str(val))
            out.append(row)
        return "\n".join(out)

    def count(self, value=True):
        """Count how many cells (in allocated chunks) equal a specific value."""
        total = 0
        for chunk in self.chunks.values():
            total += np.count_nonzero(chunk == value)
        return total
