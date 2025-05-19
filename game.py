import pygame  
import sys    
from movement import MovingObject
from objects import Ball, BALLZ

pygame.init() 
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("Pysics Engine")

LEFT, RIGHT, UP, DOWN = False, False, False, False

ball1 = Ball(100, 100, 50)
ball1.player = True

running = True

while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                LEFT = True
            elif event.key == pygame.K_RIGHT:
                RIGHT = True
            elif event.key == pygame.K_UP:
                UP = True
            elif event.key == pygame.K_DOWN:
                DOWN = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                LEFT = False
            elif event.key == pygame.K_RIGHT:
                RIGHT = False
            elif event.key == pygame.K_UP:
                UP = False
            elif event.key == pygame.K_DOWN:
                DOWN = False

    screen.fill((255, 255, 255))

    for ball in BALLZ:
        if ball.player:
            ball.move(LEFT, RIGHT, UP, DOWN)    
        ball.drawBall(screen)
        ball.display(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()

sys.exit()