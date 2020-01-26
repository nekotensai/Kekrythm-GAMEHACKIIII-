import pygame
import pygameMenu

pygame.init()
screen = pygame.display.set_mode((640, 512))
pygameMenu.Menu(screen, 640, 512, 'Comic Sans', 'Menu')
