from wall import Wall
from gate import Gate
import pyglet.graphics


class Editor:
    def __init__(self):
        self.wall_list = []
        self.gate_list = []
        self.car_position = (-1, -1)
        self.walls = False
        self.gates = False
        self.car = False
        self.mouse_x1 = 0
        self.mouse_y1 = 0
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1
        self.start_wall_x1 = -1
        self.start_wall_y1 = -1
        self.new_wall = False
        self.delete_last = False

    def show(self, window_width, window_height):
        line = pyglet.shapes.Line(0, self.mouse_y1, window_width, self.mouse_y1, 1, color=[255, 255, 255])
        line.draw()
        line = pyglet.shapes.Line(self.mouse_x1, 0, self.mouse_x1, window_height, 1, color=[255, 255, 255])
        line.draw()
        for w in self.wall_list:
            w.show()
        for g in self.gate_list:
            g.show()
        if self.car_position != (-1, -1):
            (x, y) = self.car_position
            circle = pyglet.shapes.Circle(x, y, 10, color=(50, 225, 30))
            circle.draw()

    def update(self):
        if not self.walls:
            if self.new_wall:
                self.wall_list.append(Wall(self.x1, self.y1, self.start_wall_x1, self.start_wall_y1))
                self.new_wall = False
                self.x1 = -1
                self.y1 = -1
                self.x2 = -1
                self.y2 = -1
                self.start_wall_x1 = -1
                self.start_wall_y1 = -1
            if self.x1 != -1 and self.y1 != -1 and self.x2 != -1 and self.y2 != -1:
                if self.start_wall_x1 == -1 and self.start_wall_y1 == -1:
                    self.start_wall_x1 = self.x1
                    self.start_wall_y1 = self.y1
                self.wall_list.append(Wall(self.x1, self.y1, self.x2, self.y2))
                self.x1 = self.x2
                self.y1 = self.y2
                self.x2 = -1
                self.y2 = -1
            if self.delete_last:
                self.wall_list = self.wall_list[:-1]
                self.delete_last = False
                self.x1 = self.wall_list[-1].x2
                self.y1 = self.wall_list[-1].y2
        elif not self.gates:
            if self.x1 != -1 and self.y1 != -1 and self.x2 != -1 and self.y2 != -1:
                self.gate_list.append(Gate(self.x1, self.y1, self.x2, self.y2))
                self.x1 = -1
                self.y1 = -1
                self.x2 = -1
                self.y2 = -1
            if self.delete_last:
                self.gate_list = self.gate_list[:-1]
                self.delete_last = False
        elif not self.car and self.x1 != -1 and self.y1 != -1:
            self.car_position = (self.x1, self.y1)

    def save(self):
        map_name = input("Enter map name : ")
        file_name = "./python/assets/maps/" + map_name
        f = open(file_name, "a")
        f.write("WALLS\n")
        for w in self.wall_list:
            line = str(w.x1) + "," + str(w.y1) + "," + str(w.x2) + "," + str(w.y2) + "\n"
            f.write(line)
        f.write("GATES\n")
        for g in self.gate_list:
            line = str(g.x1) + "," + str(g.y1) + "," + str(g.x2) + "," + str(g.y2) + "\n"
            f.write(line)
        f.write("CAR\n")
        (x, y) = self.car_position
        f.write(str(x) + "," + str(y))
        print("You can now close the map window to save your map")
