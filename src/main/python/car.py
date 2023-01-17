import pyglet.shapes
from maths import *


class Car:
    def __init__(self, car_position, wallList, gateList):
        global vec2
        self.wallList = wallList
        self.gateList = gateList
        (self.x, self.y) = car_position
        self.initial_position = car_position
        self.vel = 0
        self.direction = vec2(1, 0)
        self.acc = 0
        self.width = 20
        self.height = 10
        self.turningRate = 1.0 / self.width
        self.friction = 0.98
        self.maxSpeed = self.width / 2.0
        self.reverseMaxSpeed = -1 * self.maxSpeed / 2.0
        self.accelerationSpeed = self.width / 160.0
        self.dead = False
        self.carPic = pyglet.image.load("./python/assets/car.png")
        self.carSprite = pyglet.sprite.Sprite(self.carPic, x=self.x, y=self.y)
        self.carSprite.update(rotation=0, scale_x=self.width / self.carSprite.width,
                              scale_y=self.height / self.carSprite.height)
        self.turningLeft = False
        self.turningRight = False
        self.accelerating = False
        self.reversing = False
        self.stop = False
        self.score = 0
        self.gateCount = 0

    def reset(self):
        (self.x, self.y) = self.initial_position
        self.vel = 0
        self.direction = vec2(1, 0)
        self.acc = 0
        self.turningLeft = False
        self.turningRight = False
        self.accelerating = False
        self.reversing = False
        self.stop = False
        self.score = 0
        self.gateCount = 0
        self.dead = False

    def show(self):
        upVector = self.direction.rotate(90)
        drawX = self.direction.x * self.width / 2 + upVector.x * self.height / 2
        drawY = self.direction.y * self.width / 2 + upVector.y * self.height / 2
        self.carSprite.update(x=self.x - drawX, y=self.y - drawY, rotation=-get_angle(self.direction))
        self.carSprite.draw()
        self.gateList[self.gateCount].show()

    def update(self):
        if not self.dead:
            self.updateFromKeys()
            self.move()
            for w in self.wallList:
                if w.hitCar(self):
                    self.dead = True
        else:
            self.acc = 0
            self.vel = 0

    def checkGate(self, n):
        if self.gateList[self.gateCount].hitCar(self):
            self.score += n
            self.gateCount += 1
            self.gateCount = self.gateCount % len(self.gateList)
            return True
        return False

    def updateFromKeys(self):
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
                self.acc = 3 * self.accelerationSpeed
            else:
                self.acc = self.accelerationSpeed
        elif self.reversing:
            if self.vel > 0:
                self.acc = -3 * self.accelerationSpeed
            else:
                self.acc = -1 * self.accelerationSpeed

        if self.turningRight:
            self.direction = self.direction.rotate(-radiansToAngle(self.turningRate) * multiplier)
        elif self.turningLeft:
            self.direction = self.direction.rotate(radiansToAngle(self.turningRate) * multiplier)

    def move(self):
        global vec2
        self.vel += self.acc
        self.vel *= self.friction
        self.constrainVel()

        driftVector = vec2(self.direction)
        driftVector = driftVector.rotate(90)

        addVector = vec2(0, 0)
        addVector.x += self.vel * self.direction.x
        addVector.y += self.vel * self.direction.y

        if addVector.length() != 0:
            addVector.normalize()

        addVector.x * abs(self.vel)
        addVector.y * abs(self.vel)

        self.x += addVector.x
        self.y += addVector.y

    def constrainVel(self):
        if self.vel > self.maxSpeed:
            self.vel = self.maxSpeed
        elif self.vel < self.reverseMaxSpeed:
            self.vel = self.reverseMaxSpeed

    def action(self, n):
        self.turningLeft = False
        self.turningRight = False
        self.accelerating = False
        self.reversing = False
        if n == 0:
            self.accelerating = True
        elif n == 1:
            self.reversing = True
        elif n == 2:
            self.accelerating = True
            self.turningRight = True
        elif n == 3:
            self.accelerating = True
            self.turningLeft = True
        elif n == 4:
            self.reversing = True
            self.turningRight = True
        elif n == 5:
            self.reversing = True
            self.turningLeft = True
        elif n == 6:
            self.turningRight = True
        elif n == 7:
            self.turningLeft = True
