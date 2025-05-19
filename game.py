import pygame  
import sys    
from movement import Vector, Force
from objects import Ball, BALLZ

pygame.init() 
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("Pysics Engine")

LEFT, RIGHT, UP, DOWN = False, False, False, False

ball1 = Ball(100, 100, 50)
ball1.player = True
ball2 = Ball(250, 250, 30)

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
            ball.display(screen) 
        ball.drawBall(screen)
        
        distance_vector = ball.position.sub(ball1.position)

        force = Force(ball1, ball2)
        if force.collision_detection():
            force.collision_response()
            font = pygame.font.SysFont('Arial', 19)
            text = font.render("Collision Detected", True, (0, 0, 0))
            screen.blit(text, (470, 330))

    pygame.display.flip()

    clock.tick(60)


pygame.quit()

sys.exit()