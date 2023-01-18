from barrier import Barrier


class Wall(Barrier):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, [255, 0, 0])
