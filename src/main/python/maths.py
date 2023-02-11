import math
import pygame.math
import numpy as np

vec2 = pygame.math.Vector2


# This method is called to check if two lines represented by their extremities are colliding
# This function is an example of a side effect free function as
# it doesn't modify the inputted values
def lines_collided(x1, y1, x2, y2, x3, y3, x4, y4):
    v1 = [x2 - x1, y2 - y1]
    v2 = [x4 - x3, y4 - y3]
    if np.cross(v1, v2):
        u_a = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
        u_b = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
        if 0 <= u_a <= 1 and 0 <= u_b <= 1:
            return True
    return False


# This method is called to get the angle in degrees of a vector compared to a vector (1, 0)
# This function is an example of a function using a function as a return parameters :
def get_angle(vec):
    if vec.length() == 0:
        return 0
    return math.degrees(math.atan2(vec.y, vec.x))


# This method is called to convert an angle from radians to angle
def radians_to_angle(rads):
    return rads * 180 / math.pi
