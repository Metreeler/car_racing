import pyglet.graphics
from maths import *


class Gate:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = [0, 0, 255]
        self.line = pyglet.shapes.Line(self.x1, self.y1, self.x2, self.y2, 1, color=self.color)

    def show(self):
        self.line.draw()

    def hitCar(self, car):
        upVector = car.direction.rotate(90)
        hw = car.width / 2
        hh = car.height / 2
        carCorner = [vec2(car.x + car.direction.x * hw + upVector.x * hh,
                          car.y + car.direction.y * hw + upVector.y * hh),
                     vec2(car.x + car.direction.x * hw - upVector.x * hh,
                          car.y + car.direction.y * hw - upVector.y * hh),
                     vec2(car.x - car.direction.x * hw - upVector.x * hh,
                          car.y - car.direction.y * hw - upVector.y * hh),
                     vec2(car.x - car.direction.x * hw + upVector.x * hh,
                          car.y - car.direction.y * hw + upVector.y * hh)]
        for i in range(4):
            j = i + 1
            j = j % 4
            if linesCollided(self.x1, self.y1, self.x2, self.y2,
                             carCorner[i].x, carCorner[i].y, carCorner[j].x, carCorner[j].y):
                return True
        return False