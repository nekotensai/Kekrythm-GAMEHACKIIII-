import time

import pygame

d = True
a = ""
v = [1, 2, 3]


def main():
    while d:
        y = 0
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        y5 = 0
        wei = 15
        speed = 5
        sume = 0
        avalible = False
        avalible1 = False
        avalible2 = False
        avalible3 = False
        avalible4 = False
        invisible = True
        invisible1 = True
        invisible2 = True
        invisible3 = True
        invisible4 = True
        blue = False
        green = False
        red = False
        yellow = False

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

            if y1 > 530:
                invisible1 = False
                y1 = 0
                invisible1 = True
            if invisible1 and blue:
                pygame.draw.circle(x1, (0, 0, 255), (128, y1), (wei))

            if y2 > 530:
                invisible2 = False
                y2 = 0
                invisible2 = True
            if invisible2 and green:
                pygame.draw.circle(x1, (0, 255, 0), (256, y2), (wei))

            if y3 > 530:
                invisible3 = False
                y3 = 0
                invisible3 = True
            if invisible3 and red:
                pygame.draw.circle(x1, (255, 0, 0), (384, y3), (wei))

            if y4 > 530:
                invisible4 = False
                y4 = 0
                invisible4 = True
            if invisible4 and yellow:
                pygame.draw.circle(x1, (255, 255, 0), (512, y4), (wei))

            sum1 = str(sume)
            c1 = pygame.font.Font(None, 36)
            text1 = c1.render(sum1, 1, (180, 0, 0))

            x1.blit(text1, (10, 50))

            #  if avalible == False:
            #    if keys[pygame.K_q] or keys[pygame.K_w] or keys[pygame.K_e] or keys[pygame.K_r]:
            #        sume -= 1

            if avalible1 == False:
                if keys[pygame.K_q]:
                    sume -= 1

            if avalible2 == False:
                if keys[pygame.K_w]:
                    sume -= 1

            if avalible3 == False:
                if keys[pygame.K_e]:
                    sume -= 1

            if avalible4 == False:
                if keys[pygame.K_r]:
                    sume -= 1

            if y1 >= 430:
                if y1 <= 480:
                    avalible1 = True
                    if keys[pygame.K_q]:
                        # invisible1 = False
                        sume += 1
                        y1 = 0
                        invisible1 = False
                        blue = False

            if y1 < 430 or y1 > 480:
                avalible1 = False

            if y2 >= 430:
                if y2 <= 480:
                    avalible2 = True
                    if keys[pygame.K_w]:
                        # invisible2 = False
                        sume += 1
                        y2 = 0
                        invisible2 = False
                        green = False

            if y2 < 430 or y2 > 480:
                avalible2 = False

            if y3 >= 430:
                if y3 <= 480:
                    avalible3 = True
                    if keys[pygame.K_e]:
                        sume += 1
                        # invisible3 = False
                        y3 = 0
                        invisible3 = False
                        red = False

            if y3 < 430 or y3 > 480:
                avalible3 = False

            if y4 >= 430:
                if y4 <= 480:
                    avalible4 = True
                    if keys[pygame.K_r]:
                        sume += 1
                        # invisible4 = False
                        y4 = 0
                        invisible4 = False
                        yellow = False
            if y4 < 430 or y4 > 480:
                avalible4 = False

            pygame.display.flip()

            if d and invisible1 == True:
                y1 += speed
            if d and invisible2 == True:
                y2 += speed
            if d and invisible3 == True:
                y3 += speed
            if d and invisible4 == True:
                y4 += speed

            while len(v) != 0:
                mute = v.pop(0)
                if mute == 1:
                    blue = True
                    invisible1 = True
                elif mute == 2:
                    green = True
                    invisible2 = True
                elif mute == 3:
                    red = True
                    invisible3 = True
                elif mute == 4:
                    yellow = True
                    invisible4 = True
                elif mute == "_":
                    time.sleep(1)

    return 0


if __name__ == "__main__":
    main()
