from enum import Enum


class DirectionSimple(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    @property
    def dx(self):
        return self.value[0]

    @property
    def dy(self):
        return self.value[1]

    def left(self):
        order = [
            DirectionSimple.UP,
            DirectionSimple.LEFT,
            DirectionSimple.DOWN,
            DirectionSimple.RIGHT,
        ]
        return order[(order.index(self) + 1) % 4]

    def right(self):
        order = [
            DirectionSimple.UP,
            DirectionSimple.RIGHT,
            DirectionSimple.DOWN,
            DirectionSimple.LEFT,
        ]
        return order[(order.index(self) + 1) % 4]

    def reverse(self):
        return self.right().right()
