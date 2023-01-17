import math
import pygame.math
import numpy as np

vec2 = pygame.math.Vector2


def linesCollided(x1, y1, x2, y2, x3, y3, x4, y4):
    v1 = [x2 - x1, y2 - y1]
    v2 = [x4 - x3, y4 - y3]
    if np.cross(v1, v2):
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
        if 0 <= uA <= 1 and 0 <= uB <= 1:
            return True
    return False


def get_angle(vec):
    if vec.length() == 0:
        return 0
    return math.degrees(math.atan2(vec.y, vec.x))


def radiansToAngle(rads):
    return rads * 180 / math.pi
