import pyglet
from my_window import MyWindow

frameRate = 60.0

if __name__ == "__main__":
    window = MyWindow(1080, 720, "Car Game", resizable=True)
    pyglet.clock.schedule_interval(window.update, 1 / frameRate)
    pyglet.app.run()
