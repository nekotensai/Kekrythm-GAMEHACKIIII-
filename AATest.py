import os

import pygame

pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 640
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load("864big.bmp")
bgr = bg.get_rect()

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


# Colors
white = (200, 200, 200)
black = (0, 0, 255)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = None

# Game Framerate
clock = pygame.time.Clock()
FPS = 60


def main_menu():
    menu = True
    selected = "stage 1"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and selected == "stage 2":
                    selected = "stage 1"
                elif event.key == pygame.K_w and selected == "stage 3":
                    selected = "stage 2"
                elif event.key == pygame.K_w and selected == "quit":
                    selected = "stage 3"
                elif event.key == pygame.K_s and selected == "stage 3":
                    selected = "quit"
                elif event.key == pygame.K_s and selected == "stage 2":
                    selected = "stage 3"
                elif event.key == pygame.K_s and selected == "stage 1":
                    selected = "stage 2"
                if event.key == pygame.K_4:
                    if selected == "stage 1":
                        pass  ## TODO: Карту №1
                    if selected == "stage 2":
                        pass  ## TODO: Карту №2
                    if selected == "stage 3":
                        pass  ## TODO: Карту №3
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(blue)
        screen.blit(bg, bgr)
        title = text_format("KekRhythm", font, 90, yellow)
        if selected == "stage 1":
            text_stage_1 = text_format("STAGE 1", font, 75, white)
        else:
            text_stage_1 = text_format("STAGE 1", font, 75, black)
        if selected == "stage 2":
            text_stage_2 = text_format("STAGE 2", font, 75, white)
        else:
            text_stage_2 = text_format("STAGE 2", font, 75, black)
        if selected == "stage 3":
            text_stage_3 = text_format("STAGE 3", font, 75, white)
        else:
            text_stage_3 = text_format("STAGE 3", font, 75, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect = title.get_rect()
        stage_1_rect = text_stage_1.get_rect()
        stage_2_rect = text_stage_2.get_rect()
        stage_3_rect = text_stage_3.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_stage_1, (screen_width / 2 - (stage_1_rect[2] / 2), 200))
        screen.blit(text_stage_2, (screen_width / 2 - (stage_1_rect[2] / 2), 260))
        screen.blit(text_stage_3, (screen_width / 2 - (stage_1_rect[2] / 2), 320))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 380))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")


main_menu()
