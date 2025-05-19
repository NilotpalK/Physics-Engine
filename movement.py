import math
import pygame

FRICTION = 0.1

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other): # add the current vector to the argument vector
        return Vector(self.x + other.x, self.y + other.y)
    
    def sub(self, other): # subtract the current vector from the argument vector
        return Vector(self.x - other.x, self.y - other.y)
    
    def mul(self, scalar): # multiply the current vector by a scalar
        return Vector(self.x * scalar, self.y * scalar)

    def mag(self): # return the magnitude of the current vector
        return math.sqrt(self.x**2 + self.y**2)
    
    def drawVector(self, start_x, start_y, scaler, color: tuple[int, int, int], screen):
        pygame.draw.line(screen, color, (start_x, start_y), (start_x + self.x * scaler, start_y + self.y * scaler))

    def unit_vector(self):
        if(self.mag() == 0):
            return Vector(0, 0)
        return Vector(self.x / self.mag(), self.y / self.mag())
    
    def normal(self):
        return Vector(-self.y, self.x).unit_vector()
    
    @staticmethod
    def dot(vector_1, vector_2):
        return vector_1.x * vector_2.x + vector_1.y * vector_2.y

class MovingObject:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.acceleration_scalar = 2

    def move(self, LEFT, RIGHT, UP, DOWN):
        if LEFT:
            self.acceleration.x = -self.acceleration_scalar
        if RIGHT:
            self.acceleration.x = self.acceleration_scalar
        if UP:  
            self.acceleration.y = -self.acceleration_scalar
        if DOWN:
            self.acceleration.y = self.acceleration_scalar  
        if not (LEFT or RIGHT or UP or DOWN):
            self.acceleration.x = 0
            self.acceleration.y = 0
        if (LEFT and RIGHT):
            self.acceleration.x = 0
        if (UP and DOWN):
            self.acceleration.y = 0
        
        #To make the acceleration diagonally uniform
        self.acceleration = self.acceleration.unit_vector().mul(self.acceleration_scalar)
        
        self.velocity = self.velocity.add(self.acceleration)
        self.velocity = self.velocity.mul(1 - FRICTION)
        self.position = self.position.add(self.velocity)

class Force(MovingObject):
    def __init__(self, ball_1, ball_2):
        self.ball_1 = ball_1
        self.ball_2 = ball_2

    def collision_detection(self):
        if (self.ball_1.radius + self.ball_2.radius >= self.ball_2.position.sub(self.ball_1.position).mag()):
            return True
        return False

    def collision_response(self):
        #points from the center of the ball 2 to the center of the ball 1
        dist_between_centers = self.ball_1.position.sub(self.ball_2.position)
        penetration_depth = self.ball_1.radius + self.ball_2.radius - dist_between_centers.mag()
        penetration_resolution = dist_between_centers.unit_vector().mul(penetration_depth/2)
        self.ball_1.position = self.ball_1.position.add(penetration_resolution)
        self.ball_2.position = self.ball_2.position.add(penetration_resolution.mul(-1))

