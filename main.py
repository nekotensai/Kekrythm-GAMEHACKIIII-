import pygame
d = True
a = ""

def main():
    while d:
        x = 128
        y = 0
        wei = 15
        speed = 5
        g = True

        a = True
        pygame.init()
        x1 = pygame.display.set_mode((640, 512))

        pygame.display.set_caption("KekRythm")

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
            pygame.draw.line(x1, (255, 255, 255), (0, 475), (640, 475), 1)
            pygame.draw.line(x1, (0, 0, 255), (128, 0), (128, 512), 1)
            pygame.draw.line(x1, (0, 255, 0), (256, 0), (256, 512), 1)
            pygame.draw.line(x1, (255, 0, 0), (384, 0), (384, 512), 1)
            pygame.draw.line(x1, (255, 255, 0), (512, 0), (512, 512), 1)
            pygame.draw.circle(x1, (255, 255, 255), (128, 475), 17)
            pygame.draw.circle(x1, (0, 0, 0), (128, 475), 15)
            pygame.draw.circle(x1, (255, 255, 255), (256, 475), 17)
            pygame.draw.circle(x1, (0, 0, 0), (256, 475), 15)
            pygame.draw.circle(x1, (255, 255, 255), (384, 475), 17)
            pygame.draw.circle(x1, (0, 0, 0), (384, 475), 15)
            pygame.draw.circle(x1, (255, 255, 255), (512, 475), 17)
            pygame.draw.circle(x1, (0, 0, 0), (512, 475), 15)

            if y == 500:
                g = False
            if g:
                pygame.draw.circle(x1, (0, 0, 255), (128, y), (wei))
                pygame.draw.circle(x1, (0, 255, 0), (256, y), (wei))
                pygame.draw.circle(x1, (255, 0, 0), (384, y), (wei))
                pygame.draw.circle(x1, (255, 255, 0), (512, y), (wei))

            pygame.display.flip()

            if d:
                y += speed

    return 0

if __name__ == "__main__":
    main()
