from car import Car
from wall import Wall
from gate import Gate


class Game:
    def __init__(self, map_name):
        self.wallList = []
        self.gateList = []
        self.car_position = (0, 0)
        self.load_map(map_name)

        self.car = Car(self.car_position)

    def show(self):
        self.car.show()
        for w in self.wallList:
            w.show()
        for g in self.gateList:
            g.show()

    def update(self, size):
        self.car.update()

    def load_map(self, map_name):
        self.wallList = []
        wall_reading = False
        self.gateList = []
        gate_reading = False
        self.car_position = (0, 0)
        car_reading = False
        f = open("./python/assets/" + map_name, "r")
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
                    self.wallList.append(Wall(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
                elif gate_reading:
                    data = line.split(",")
                    self.gateList.append(Gate(int(data[0]), int(data[1]), int(data[2]), int(data[3])))
                elif car_reading:
                    data = line.split(",")
                    self.car_position = (int(data[0]), int(data[1]))
        f.close()
