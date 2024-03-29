import pyglet
from os import listdir
from src.main.python.my_window import MyWindow

frame_rate = 60.0
playing_editing = True

if __name__ == "__main__":
    while playing_editing:
        i = input("Do you want to play (p) or do you want to create map (m) : ")
        # This part is called when the user wants to play
        if i == "p":
            # First we chose the map we want to play on
            map_list = listdir("./python/assets/maps")
            print(map_list)
            map_name = ""
            while map_name not in map_list:
                map_name = input("Which map from above do you want to play : ")
                if map_name not in map_list:
                    print("Not a valid map name, try again")
            print("Use the directional arrows to move the car around and try to hit as many blue walls as possible !")
            print("Press UP to go forward and press LEFT and RIGHT to navigate, you can go backward by pressing DOWN")
            playing_editing = False
            # The window is created then displayed
            window = MyWindow(False, map_name, 1080, 720, "Car Game", resizable=True)
            pyglet.clock.schedule_interval(window.update, 1 / frame_rate)
            pyglet.app.run()
        elif i == "m":
            playing_editing = False
            # The window is created then displayed
            window = MyWindow(True, "", 1080, 720, "Car Game", resizable=True)
            pyglet.clock.schedule_interval(window.update, 1 / frame_rate)
            pyglet.app.run()
        else:
            # Called if the entry is wrong
            print(i + " is not a valid answer")
