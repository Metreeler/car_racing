from src.main.python.car import Car
from src.main.python.wall import Wall
from src.main.python.gate import Gate


class Game:
    # Initialization of the Game class
    def __init__(self, map_name):
        self.wall_list = []
        self.gate_list = []
        self.car_position = (0, 0)
        self.load_map(map_name)

        self.car = Car(self.car_position, self.wall_list, self.gate_list)

    # This method is called to display the element of the game
    def show(self):
        self.car.show()
        for w in self.wall_list:
            w.show()

    # This method is called to update the element of the game
    def update(self):
        self.car.update()

    # This method is called during the initialization to load the map and its characteristics
    def load_map(self, map_name):
        self.wall_list = []
        wall_reading = False
        self.gate_list = []
        gate_reading = False
        self.car_position = (0, 0)
        car_reading = False
        f = open("./python/assets/maps/" + map_name, "r")
        for line in f:
            line = line.split("\n")[0]
            if line == "WALLS":
                wall_reading = True
                gate_reading = False
                car_reading = False
            elif line == "GATES":
                gate_reading = True
                wall_reading = False
                car_reading = False
            elif line == "CAR":
                car_reading = True
                gate_reading = False
                wall_reading = False
            else:
                if wall_reading:
                    data = line.split(",")
                    self.wall_list.append(Wall(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
                elif gate_reading:
                    data = line.split(",")
                    self.gate_list.append(Gate(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
                elif car_reading:
                    data = line.split(",")
                    self.car_position = (int(data[0]), int(data[1]))
        f.close()
