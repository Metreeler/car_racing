import pyglet
from src.main.python.game import Game
from src.main.python.editor import Editor


# This class derives from the pyglet window
class MyWindow(pyglet.window.Window):
    # This method initialize the window while being careful if we are in editor mode or if we are in player mode
    def __init__(self, editing, map_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        (self.window_width, self.window_height) = self.get_size()
        self.background = pyglet.shapes.Rectangle(0, 0, self.window_width, self.window_height, color=[200, 200, 200])
        self.editing = editing
        if self.editing:
            self.editor = Editor()
        else:
            self.game = Game(map_name)

    # This method is called on every frame to display chat is needed
    def on_draw(self):
        self.background.draw()
        if self.editing:
            self.editor.show(self.window_width, self.window_height)
        else:
            self.game.show()

    # This method is called whenever to update the game or the editor
    def update(self, dt):
        if (self.window_width, self.window_height) != self.get_size():
            (self.window_width, self.window_height) = self.get_size()
        self.background.width, self.background.height = self.window_width, self.window_height
        if self.editing:
            self.editor.update()
        else:
            self.game.update()

    # This method is called everytime a key is pressed
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
                    print("Now create the gates for the scores "
                          "(create gates : MOUSE CLICK, delete : BACKSPACE, save : ENTER)")
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
                    self.editor.gates = True
                    print("Now click on the starting point of the race")
                elif symbol == pyglet.window.key.BACKSPACE:
                    self.editor.delete_last = True
            elif not self.editor.car:
                if symbol == pyglet.window.key.ENTER:
                    map_name = input("Enter map name : ")
                    self.editor.save("./python/assets/maps/" + map_name)
        else:
            if symbol == pyglet.window.key.RIGHT:
                self.game.car.turning_right = True
            elif symbol == pyglet.window.key.LEFT:
                self.game.car.turning_left = True
            if symbol == pyglet.window.key.UP:
                self.game.car.accelerating = True
            elif symbol == pyglet.window.key.DOWN:
                self.game.car.reversing = True
            if symbol == pyglet.window.key.SPACE:
                self.game.car.stop = True
            if symbol == pyglet.window.key.R:
                self.game.car.reset()

    # This method is called everytime a key is released
    def on_key_release(self, symbol, modifiers):
        if not self.editing:
            if symbol == pyglet.window.key.RIGHT:
                self.game.car.turning_right = False
            if symbol == pyglet.window.key.LEFT:
                self.game.car.turning_left = False
            if symbol == pyglet.window.key.UP:
                self.game.car.accelerating = False
            if symbol == pyglet.window.key.DOWN:
                self.game.car.reversing = False
            if symbol == pyglet.window.key.SPACE:
                self.game.car.stop = False

    # This method is called everytime the mouse is pressed
    def on_mouse_press(self, x, y, button, modifiers):
        if self.editing:
            if self.editor.x1 == -1 and self.editor.y1 == -1:
                self.editor.x1 = x
                self.editor.y1 = y
            elif self.editor.x2 == -1 and self.editor.y2 == -1:
                self.editor.x2 = x
                self.editor.y2 = y

    # This method is called everytime the mouse is moved
    def on_mouse_motion(self, x, y, dx, dy):
        if self.editing:
            self.editor.mouse_x1 = x
            self.editor.mouse_y1 = y








