import pygame
d = True
a = ""
def main():
    while d:
        a = True
        pygame.init()
        x1 = pygame.display.set_mode((500, 500))

        pygame.display.set_caption("KickRythm")

        run = True
        a1 = 0
        while run:
            pygame.time.delay(50)
    return 0

if __name__ == "__main__":
    main()
