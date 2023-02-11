import pyglet.graphics
from src.main.python.maths import vec2, lines_collided


class Barrier:
    # Initialization of the Barrier class
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.line = pyglet.shapes.Line(self.x1, self.y1, self.x2, self.y2, 1, color=self.color)

    # This method is called to display the barrier
    def show(self):
        self.line.draw()

    # This method is called to check if the barrier is hitting a car
    def hit_car(self, car):
        up_vector = car.direction.rotate(90)
        hw = car.width / 2
        hh = car.height / 2
        car_corner = [vec2(car.x + car.direction.x * hw + up_vector.x * hh,
                           car.y + car.direction.y * hw + up_vector.y * hh),
                      vec2(car.x + car.direction.x * hw - up_vector.x * hh,
                           car.y + car.direction.y * hw - up_vector.y * hh),
                      vec2(car.x - car.direction.x * hw - up_vector.x * hh,
                           car.y - car.direction.y * hw - up_vector.y * hh),
                      vec2(car.x - car.direction.x * hw + up_vector.x * hh,
                           car.y - car.direction.y * hw + up_vector.y * hh)]
        for i in range(4):
            j = i + 1
            j = j % 4
            if lines_collided(self.x1, self.y1, self.x2, self.y2,
                              car_corner[i].x, car_corner[i].y, car_corner[j].x, car_corner[j].y):
                return True
        return False
