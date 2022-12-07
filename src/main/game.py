import pyglet
from car import Car


class Game:
    def __init__(self, size):
        (self.window_width, self.window_height) = size
        self.background = pyglet.shapes.Rectangle(0, 0, self.window_width, self.window_height, color=[200, 200, 200])
        self.car = Car(self.window_width / 2, self.window_height / 2)

    def show(self):
        self.background.draw()
        self.car.show()

    def update(self, size):
        if (self.window_width, self.window_height) != size:
            (self.window_width, self.window_height) = size
        self.background.width, self.background.height = self.window_width, self.window_height
        self.car.update()
