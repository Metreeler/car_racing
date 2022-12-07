import pyglet.shapes
from math import *


class Car:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.vel = 0
        self.width = 12
        self.length = 30
        self.rotation_angle = 0
        self.rotating = 0
        self.texture = pyglet.shapes.Rectangle(self.x - self.length / 2,
                                               self.y - self.width / 2,
                                               self.length,
                                               self.width,
                                               color=[255, 0, 0])
        self.texture.anchor_x = self.length / 2
        self.texture.anchor_y = self.width / 2

    def show(self):
        self.texture.x = self.x
        self.texture.y = self.y
        self.texture.rotation = self.rotation_angle
        self.texture.draw()

    def update(self):
        self.rotation_angle += self.rotating
        self.rotation_angle = self.rotation_angle % 360
        self.x += self.vel * cos(radians(-self.rotation_angle))
        self.y += self.vel * sin(radians(-self.rotation_angle))
