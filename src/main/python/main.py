import pyglet
from os import listdir
from src.main.python.my_window import MyWindow

frame_rate = 60.0
playing_editing = True

if __name__ == "__main__":
    while playing_editing:
        i = input("Do you want to play (p) or do you want to create map (m) : ")
        if i == "p":
            map_list = listdir("./python/assets/maps")
            print(map_list)
            map_name = ""
            while map_name not in map_list:
                map_name = input("Which map from above do you want to play : ")
                if map_name not in map_list:
                    print("Not a valid map name, try again")
            playing_editing = False
            window = MyWindow(False, map_name, 1080, 720, "Car Game", resizable=True)
            pyglet.clock.schedule_interval(window.update, 1 / frame_rate)
            pyglet.app.run()
        elif i == "m":
            playing_editing = False
            window = MyWindow(True, "", 1080, 720, "Car Game", resizable=True)
            pyglet.clock.schedule_interval(window.update, 1 / frame_rate)
            pyglet.app.run()
        else:
            print(i + " is not a valid answer")
