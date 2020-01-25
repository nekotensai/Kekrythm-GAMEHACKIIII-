import time
import pygame

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
v = [('G',28),('B',50),('R',100)]
color = {'B':512//4,'G':512*2//4,'Y':512*3//4,'R':512*4//4}
fps = 60
clock = pygame.time.Clock()


class slider():
    def __init__(self, x, length, screen, velocity):
        self.r = 15
        self.b = 1
        self.length = length * velocity * fps
        self.x = x
        self.y = 0 - self.r - self.length
        self.screen = screen
        self.velocity = velocity
        self.color = (255, 255, 255)

    def move():
        self.y += self.velocity

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, self.color, (self.x, self.y + self.length), self.r)
        pygame.draw.rect(self.screen, self.color, (self.x - self.r, self.y , self.r * 2, self.length), self.b)

    def move(self):
        self.y += self.velocity

    def __del__(self):
        self.y = 512
        self.color = (0,0,0)
        self.b = 0


class note():
    def __init__(self, x, screen, velocity):
        self.r = 15
        self.x = x
        self.y = 0 - self.r
        self.screen = screen
        self.velocity = velocity
        self.color = (255, 255, 255)

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
    mas = []
    points = 0
    timer = 0

    while True:
        screen = pygame.display.set_mode((640, 512))
        if temp == 0:
            a = slider(100, 1, screen, 3)

        draw_field(screen)

        a.draw()
        a.move()

        pygame.display.flip()

        clock.tick(fps)
        temp += 1


def draw_field(screen):
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


if __name__ == "__main__":
    main()