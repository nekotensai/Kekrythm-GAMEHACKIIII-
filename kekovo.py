import time
import pygame

pygame.init()
v = [('Y',28),('Y',50),('Y',100)]
color = {'B':512//4,'G':512*2//4,'Y':512*3//4,'R':512*4//4,}

class note():
    def __init__(self, x, screen, velocity):
        self.r = 15
        self.x = x
        self.y = 0 - self.r
        self.screen = screen
        self.velocity = velocity

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (self.x, self.y), self.r)
    def move(self):
        self.y += self.velocity
    def __del__(self):
        pass

def main():
    temp = 0
    mas = []
    while True:
        screen = pygame.display.set_mode((640, 512))

        pygame.display.set_caption("KekRythm")
        pygame.draw.line(screen, (255, 255, 255), (0, 455), (640, 455), 1)
        pygame.draw.line(screen, (0, 0, 255), (128, 0), (128, 512), 1)
        pygame.draw.line(screen, (0, 255, 0), (256, 0), (256, 512), 1)
        pygame.draw.line(screen, (255, 255, 0), (384, 0), (384, 512), 1)
        pygame.draw.line(screen, (255, 0, 0), (512, 0), (512, 512), 1)
        pygame.draw.circle(screen, (255, 255, 255), (128, 455), 17)
        pygame.draw.circle(screen, (0, 0, 0), (128, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (256, 455), 17)
        pygame.draw.circle(screen, (0, 0, 0), (256, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (384, 455), 17)
        pygame.draw.circle(screen, (0, 0, 0), (384, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (512, 455), 17)
        pygame.draw.circle(screen, (0, 0, 0), (512, 455), 15)


        if v[0][1] == temp:
            mas.append(note(color[v[0][0]], screen, 3))
            v.pop(0)
            if len(v) == 0:v.append((0,-1))

        for i in mas:
        	if i.y > 512:
        		del i
        	else:
        		i.draw()
        		i.move()

        pygame.display.flip()

        pygame.time.delay(20)
        temp += 1


if __name__ == "__main__":
    main()