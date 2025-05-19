import pygame
from movement import MovingObject

# List to store all ball objects
BALLZ = []

class Ball(MovingObject):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius
        self.player = False
        BALLZ.append(self)
        
    def drawBall(self, screen):
        #fill the ball with a color
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
        #ball outline
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.radius, 1)
    
    def display(self, screen):
        # Draw acceleration vector (blue line)
        self.acceleration.unit_vector().drawVector(550, 400, 50, (0, 0, 255), screen)
        # Draw velocity vector (green line)
        self.velocity.drawVector(550, 400, 10, (0, 255, 0), screen)
        # Get a vector direction map
        pygame.draw.circle(screen, (0,0,0), (550, 400), self.radius, 1)