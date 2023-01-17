import pyglet
from my_window import MyWindow

frameRate = 60.0
playing_editing = True

if __name__ == "__main__":
    while playing_editing:
        i = input("Do you want to play (p) or do you want to create map (m) : ")
        if i == "p":
            playing_editing = False
            window = MyWindow(1080, 720, "Car Game", resizable=True)
            pyglet.clock.schedule_interval(window.update, 1 / frameRate)
            pyglet.app.run()
        elif i == "m":
            playing_editing = False
        else:
            print(i + " is not a valid answer")
