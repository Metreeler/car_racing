from src.main.python.barrier import Barrier


class Gate(Barrier):
    # Initialization of the Gate class as a child of the barrier class
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2, [0, 0, 255])
