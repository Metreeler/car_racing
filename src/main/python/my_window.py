import pyglet
from game import Game


class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        self.game = Game(self.get_size())

    def on_draw(self):
        self.game.show()

    def update(self, dt):
        self.game.update(self.get_size())

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            self.game.car.vel = 10
        elif symbol == pyglet.window.key.DOWN:
            self.game.car.vel = -5
        if symbol == pyglet.window.key.RIGHT:
            self.game.car.rotating = 5
        elif symbol == pyglet.window.key.LEFT:
            self.game.car.rotating = -5

    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP or symbol == pyglet.window.key.DOWN:
            self.game.car.vel = 0
        if symbol == pyglet.window.key.RIGHT or symbol == pyglet.window.key.LEFT:
            self.game.car.rotating = 0
