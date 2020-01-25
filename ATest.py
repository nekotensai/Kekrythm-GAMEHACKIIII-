import pygame
pygame.init()
screen = pygame.display.set_mode((640, 512))
pygame.display.set_caption("KekRythm")
while 1:
    screen.fill((0, 0, 0))
    pygame.draw.line()
    pygame.draw.circle(screen, (0, 255, 0), (155, 20), 10)
    pygame.display.flip()
