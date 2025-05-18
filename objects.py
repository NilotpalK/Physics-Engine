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
        # Draw acceleration vector (green line)
        pygame.draw.line(
            screen, 
            (0, 255, 0),  # Green color
            (self.x, self.y),  # Start at ball position
            (self.x + self.acceleration_x * 100, self.y + self.acceleration_y * 100)  # Multiply by 100 to make visible
        )
        
        # Draw velocity vector (blue line)
        pygame.draw.line(
            screen, 
            (0, 0, 255),  # Blue color
            (self.x, self.y),  # Start at ball position
            (self.x + self.velocity_x * 10, self.y + self.velocity_y * 10)  # Multiply by 10 to make visible
        )
        