import pyglet.clock
from my_window import MyWindow

frameRate = 30.0

if __name__ == "__main__":
    window = MyWindow(1080, 720, "Car Game", resizable=True, fullscreen=False)
    pyglet.clock.schedule_interval(window.update, 1 / frameRate)
    pyglet.app.run()
