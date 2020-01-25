import pygame
d = True
a = ""

def main():
    while d:
        y = 0
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        wei = 15
        speed = 5
        invisible = True
        invisible1 = True
        invisible2 = True
        invisible3 = True
        invisible4 = True

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
            pygame.draw.line(x1, (255, 255, 255), (0, 455), (640, 455), 1)
            pygame.draw.line(x1, (0, 0, 255), (128, 0), (128, 512), 1)
            pygame.draw.line(x1, (0, 255, 0), (256, 0), (256, 512), 1)
            pygame.draw.line(x1, (255, 0, 0), (384, 0), (384, 512), 1)
            pygame.draw.line(x1, (255, 255, 0), (512, 0), (512, 512), 1)
            pygame.draw.circle(x1, (255, 255, 255), (128, 455), 17)
            pygame.draw.circle(x1, (0, 0, 0), (128, 455), 15)
            pygame.draw.circle(x1, (255, 255, 255), (256, 455), 17)
            pygame.draw.circle(x1, (0, 0, 0), (256, 455), 15)
            pygame.draw.circle(x1, (255, 255, 255), (384, 455), 17)
            pygame.draw.circle(x1, (0, 0, 0), (384, 455), 15)
            pygame.draw.circle(x1, (255, 255, 255), (512, 455), 17)
            pygame.draw.circle(x1, (0, 0, 0), (512, 455), 15)

            # if y > 510:
            #    invisible = False
            # if invisible:
            #    pygame.draw.circle(x1, (0, 0, 255), (128, y), (wei))
            #    pygame.draw.circle(x1, (0, 255, 0), (256, y), (wei))
            #    pygame.draw.circle(x1, (255, 0, 0), (384, y), (wei))
            #    pygame.draw.circle(x1, (255, 255, 0), (512, y), (wei))

            if y1 > 530:
                invisible1 = False
                y1 = 0
                invisible1 = True
            if invisible1:
                pygame.draw.circle(x1, (0, 0, 255), (128, y1), (wei))

            if y2 > 530:
                invisible2 = False
                y2 = 0
                invisible2 = True
            if invisible2:
                pygame.draw.circle(x1, (0, 255, 0), (256, y2), (wei))

            if y3 > 530:
                invisible3 = False
                y3 = 0
                invisible3 = True
            if invisible3:
                pygame.draw.circle(x1, (255, 0, 0), (384, y3), (wei))

            if y4 > 530:
                invisible4 = False
                y4 = 0
                invisible4 = True
            if invisible4:
                pygame.draw.circle(x1, (255, 255, 0), (512, y4), (wei))

            if y1 >= 440:
                if y1 <= 470:
                    if keys[pygame.K_q]:
                        invisible1 = False
                        y1 = 0
                        invisible1 = True

            if y2 >= 440:
                if y2 <= 470:
                    if keys[pygame.K_w]:
                        invisible2 = False
                        y2 = 0
                        invisible2 = True

            if y3 >= 440:
                if y3 <= 470:
                    if keys[pygame.K_e]:
                        invisible3 = False
                        y3 = 0
                        invisible3 = True

            if y4 >= 440:
                if y4 <= 470:
                    if keys[pygame.K_r]:
                        invisible4 = False
                        y4 = 0
                        invisible4 = True

            pygame.display.flip()

            if d:
                y1 += speed
            if d:
                y2 += speed
            if d:
                y3 += speed
            if d:
                y4 += speed
    return 0


if __name__ == "__main__":
    main()
