import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 512))
ball = pygame.image.load('1.png')
ballrect = ball.get_rect()
speed = [2, 2]
black = 0, 0, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > 640:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 512:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

