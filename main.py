import pygame
d = True
a = ""

def main():
    while d:
        x = 100
        y = 100
        wei = 10
        hei = 10
        speed = 5

        a = True
        pygame.init()
        x1 = pygame.display.set_mode((500, 500))

        pygame.display.set_caption("KickRythm")

        run = True
        a1 = 0
        while run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    exit()

            keys = pygame.key.get_pressed()

            x1.fill((0, 0, 0))
            if y != 480:
                pygame.draw.circle(x1, (0, 0, 255), (x, y), (wei))

            pygame.display.flip()

            if y < 500 - wei - 10:
                y += speed

    return 0

if __name__ == "__main__":
    main()
