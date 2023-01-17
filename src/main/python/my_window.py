import pyglet
from game import Game
from editor import Editor


class MyWindow(pyglet.window.Window):
    def __init__(self, editing, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        (self.window_width, self.window_height) = self.get_size()
        self.background = pyglet.shapes.Rectangle(0, 0, self.window_width, self.window_height, color=[200, 200, 200])
        self.editing = editing
        if self.editing:
            self.editor = Editor()
        else:
            self.game = Game("map1")

    def on_draw(self):
        self.background.draw()
        if self.editing:
            self.editor.show(self.window_width, self.window_height)
        else:
            self.game.show()

    def update(self, dt):
        if (self.window_width, self.window_height) != self.get_size():
            (self.window_width, self.window_height) = self.get_size()
        self.background.width, self.background.height = self.window_width, self.window_height
        if self.editing:
            self.editor.update()
        else:
            self.game.update(self.get_size())

    def on_key_press(self, symbol, modifiers):
        if self.editing:
            if not self.editor.walls:
                if symbol == pyglet.window.key.ENTER:
                    self.editor.x1 = -1
                    self.editor.y1 = -1
                    self.editor.x2 = -1
                    self.editor.y2 = -1
                    self.editor.start_wall_x1 = -1
                    self.editor.start_wall_y1 = -1
                    self.editor.walls = True
                elif symbol == pyglet.window.key.N:
                    self.editor.new_wall = True
                elif symbol == pyglet.window.key.BACKSPACE:
                    self.editor.delete_last = True
            elif not self.editor.gates:
                if symbol == pyglet.window.key.ENTER:
                    self.editor.x1 = -1
                    self.editor.y1 = -1
                    self.editor.x2 = -1
                    self.editor.y2 = -1
                    self.editor.start_wall_x1 = -1
                    self.editor.start_wall_y1 = -1
                    self.editor.gates = True
                elif symbol == pyglet.window.key.BACKSPACE:
                    self.editor.delete_last = True
            elif not self.editor.car:
                if symbol == pyglet.window.key.ENTER:
                    self.editor.save()
        else:
            if symbol == pyglet.window.key.UP:
                self.game.car.vel = 10
            elif symbol == pyglet.window.key.DOWN:
                self.game.car.vel = -5
            if symbol == pyglet.window.key.RIGHT:
                self.game.car.rotating = 5
            elif symbol == pyglet.window.key.LEFT:
                self.game.car.rotating = -5

    def on_key_release(self, symbol, modifiers):
        if self.editing:
            pass
        else:
            if symbol == pyglet.window.key.UP or symbol == pyglet.window.key.DOWN:
                self.game.car.vel = 0
            if symbol == pyglet.window.key.RIGHT or symbol == pyglet.window.key.LEFT:
                self.game.car.rotating = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.editing:
            if self.editor.x1 == -1 and self.editor.y1 == -1:
                self.editor.x1 = x
                self.editor.y1 = y
            elif self.editor.x2 == -1 and self.editor.y2 == -1:
                self.editor.x2 = x
                self.editor.y2 = y

    def on_mouse_motion(self, x, y, dx, dy):
        if self.editing:
            self.editor.mouse_x1 = x
            self.editor.mouse_y1 = y








