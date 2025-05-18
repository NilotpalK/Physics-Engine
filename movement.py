import math

FRICTION = 0.1

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other): # add the current vector to the argument vector
        return Vector(self.x + other.x, self.y + other.y)
    
    def sub(self, other): # subtract the current vector from the argument vector
        return Vector(self.x - other.x, self.y - other.y)

    def mag(self): # return the magnitude of the current vector
        return math.sqrt(self.x**2 + self.y**2)

class MovingObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.acceleration = 1

    def move(self, LEFT, RIGHT, UP, DOWN):
        if LEFT:
            self.acceleration_x = -self.acceleration
        elif RIGHT:
            self.acceleration_x = self.acceleration
        if UP:  
            self.acceleration_y = -self.acceleration
        elif DOWN:
            self.acceleration_y = self.acceleration
        if not (LEFT or RIGHT or UP or DOWN):
            self.acceleration_x = 0
            self.acceleration_y = 0
        if (LEFT and RIGHT):
            self.acceleration_x = 0
        if (UP and DOWN):
            self.acceleration_y = 0
        
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        self.velocity_x *= 1 - FRICTION
        self.velocity_y *= 1 - FRICTION
        self.x += self.velocity_x
        self.y += self.velocity_y
