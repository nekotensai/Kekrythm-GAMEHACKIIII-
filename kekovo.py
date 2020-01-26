import time
import pygame

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
v = [('N','G',28),('N','B',50),('S','R',100,60),('N','B',130)]
color = {'B':512//4,'G':512*2//4,'Y':512*3//4,'R':512*4//4}
colors = {'B':(0,0,255),'G':(0,255,0),'Y':(255,255,0),'R':(255,0,0)}
fps = 60
clock = pygame.time.Clock()


class slider():
    def __init__(self, x, screen, velocity, color, length):
        self.r = 15
        self.b = 1
        self.length = length * velocity
        self.x = x
        self.y = 0 - self.r - self.length
        self.screen = screen
        self.velocity = velocity
        self.color = colors[color]

    def move():
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, self.color, (self.x, self.y + self.length), self.r)
        pygame.draw.rect(self.screen, self.color, (self.x - self.r, self.y , self.r * 2, self.length))

    def move(self):
        self.y += self.velocity

    def __del__(self):
        self.y = 512
        self.color = (0,0,0)
        self.b = 0


class note():
    def __init__(self, x, screen, velocity, color):
        self.r = 15
        self.x = x
        self.y = 0 - self.r
        self.screen = screen
        self.velocity = velocity
        self.color = colors[color]

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.y += self.velocity

    def __del__(self):
        self.y = 512
        self.color = (0,0,0)
        self.r = 0


def main():
    temp = 0
    notes = []
    sliders = []
    points = 0
    timer = 0
    while True:
        screen = pygame.display.set_mode((640, 512))

        draw_field(screen)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYUP:
                # flag = False
                if i.key == pygame.K_q:
                    xtemp = 512//4
                elif i.key == pygame.K_w:
                    xtemp = 512*2//4
                elif i.key == pygame.K_e:
                    xtemp = 512*3//4
                elif i.key == pygame.K_r:
                    xtemp = 512*4//4
                elif i.key == pygame.K_u:
                    exit()
                else:
                    xtemp = -100

                for i in notes:
                    if i.y < 465 and i.y > 445 and i.x == xtemp:
                        points += 1
                        i.__del__()

                for i in sliders:
                    i[1] += 1
                    if i[0].y < 465 and i[0].y + i[0].length > 445 and i[0].x == xtemp:
                        if i[1] >= 7:
                            i[1] = 0
                            points += 1


                        # flag = True
                # if not flag:
                #     points -=1

        if v[0][2] == temp:
            if v[0][0] == 'N':
                notes.append(note(color[v[0][1]], screen, 3, v[0][1]))

            elif v[0][0] == 'S':
                sliders.append([slider(color[v[0][1]],screen, 3, v[0][1], v[0][3]),10])

            v.pop(0)
            if len(v) == 0:
                v.append((0, 0, -1))

        for i in notes:
            if i.y > 512:
                del i
            else:
                i.draw()
                i.move()

        for i in sliders:
            if i[0].y > 512:
                del i
            else:
                i[0].draw()
                i[0].move()

        textsurface = myfont.render(str(points), False, (255, 255, 255))
        screen.blit(textsurface,(50,10))

        pygame.display.flip()

        clock.tick(fps)
        temp += 1


def draw_field(screen):
        pygame.display.set_caption("KekRythm")
        pygame.draw.rect(screen,(100, 100, 100), (0, 0, 640, 512))
        # pygame.draw.line(screen, (0, 0, 0), (0, 455), (640, 455), 1)
        pygame.draw.line(screen, (0, 0, 255), (128, 0), (128, 512), 3)
        pygame.draw.line(screen, (0, 255, 0), (256, 0), (256, 512), 3)
        pygame.draw.line(screen, (255, 255, 0), (384, 0), (384, 512), 3)
        pygame.draw.line(screen, (255, 0, 0), (512, 0), (512, 512), 3)

        pygame.draw.circle(screen, (255, 255, 255), (128, 455), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (128, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (256, 455), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (256, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (384, 455), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (384, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (512, 455), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (512, 455), 15)


if __name__ == "__main__":
    main()