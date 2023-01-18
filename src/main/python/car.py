import pyglet.shapes
from maths import get_angle, radians_to_angle, vec2


class Car:
    def __init__(self, car_position, wall_list, gate_list):
        global vec2
        self.wall_list = wall_list
        self.gate_list = gate_list
        (self.x, self.y) = car_position
        self.initial_position = car_position
        self.vel = 0
        self.direction = vec2(1, 0)
        self.acc = 0
        self.width = 20
        self.height = 10
        self.turning_rate = 2.0 / self.width
        self.friction = 0.98
        self.max_speed = self.width / 2.0
        self.reverse_max_speed = -1 * self.max_speed / 2.0
        self.acceleration_speed = self.width / 160.0
        self.dead = False
        self.car_picture = pyglet.image.load("./python/assets/car.png")
        self.car_sprite = pyglet.sprite.Sprite(self.car_picture, x=self.x, y=self.y)
        self.car_sprite.update(rotation=0, scale_x=self.width / self.car_sprite.width,
                              scale_y=self.height / self.car_sprite.height)
        self.turning_left = False
        self.turning_right = False
        self.accelerating = False
        self.reversing = False
        self.stop = False
        self.score = 0
        self.gate_count = 0

    def reset(self):
        (self.x, self.y) = self.initial_position
        self.vel = 0
        self.direction = vec2(1, 0)
        self.acc = 0
        self.turning_left = False
        self.turning_right = False
        self.accelerating = False
        self.reversing = False
        self.stop = False
        self.score = 0
        self.gate_count = 0
        self.dead = False

    def show(self):
        up_vector = self.direction.rotate(90)
        draw_x = self.direction.x * self.width / 2 + up_vector.x * self.height / 2
        draw_y = self.direction.y * self.width / 2 + up_vector.y * self.height / 2
        self.car_sprite.update(x=self.x - draw_x, y=self.y - draw_y, rotation=-get_angle(self.direction))
        self.car_sprite.draw()
        self.gate_list[self.gate_count].show()

    def update(self):
        if not self.dead:
            self.update_from_keys()
            self.move()
            self.check_gate(self.gate_count)
            for w in self.wall_list:
                if w.hit_car(self):
                    self.dead = True
        else:
            self.acc = 0
            self.vel = 0

    def check_gate(self, n):
        if self.gate_list[self.gate_count].hit_car(self):
            self.score += n
            self.gate_count += 1
            self.gate_count = self.gate_count % len(self.gate_list)
            return True
        return False

    def update_from_keys(self):
        self.acc = 0

        if self.stop:
            self.vel = 0

        multiplier = 1
        if abs(self.vel) < 5:
            multiplier = abs(self.vel) / 5
        if self.vel < 0:
            multiplier *= -1

        if self.accelerating:
            if self.vel < 0:
                self.acc = 3 * self.acceleration_speed
            else:
                self.acc = self.acceleration_speed
        elif self.reversing:
            if self.vel > 0:
                self.acc = -3 * self.acceleration_speed
            else:
                self.acc = -1 * self.acceleration_speed

        if self.turning_right:
            self.direction = self.direction.rotate(-radians_to_angle(self.turning_rate) * multiplier)
        elif self.turning_left:
            self.direction = self.direction.rotate(radians_to_angle(self.turning_rate) * multiplier)

    def move(self):
        global vec2
        self.vel += self.acc
        self.vel *= self.friction
        self.constrain_vel()

        add_vector = vec2(0, 0)
        add_vector.x += self.vel * self.direction.x
        add_vector.y += self.vel * self.direction.y

        if add_vector.length() != 0:
            add_vector.normalize()

        self.x += add_vector.x
        self.y += add_vector.y

    def constrain_vel(self):
        if self.vel > self.max_speed:
            self.vel = self.max_speed
        elif self.vel < self.reverse_max_speed:
            self.vel = self.reverse_max_speed

    def action(self, n):
        self.turning_left = False
        self.turning_right = False
        self.accelerating = False
        self.reversing = False
        if n == 0:
            self.accelerating = True
        elif n == 1:
            self.reversing = True
        elif n == 2:
            self.accelerating = True
            self.turning_right = True
        elif n == 3:
            self.accelerating = True
            self.turning_left = True
        elif n == 4:
            self.reversing = True
            self.turning_right = True
        elif n == 5:
            self.reversing = True
            self.turning_left = True
        elif n == 6:
            self.turning_right = True
        elif n == 7:
            self.turning_left = True
