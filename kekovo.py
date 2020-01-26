import time
import pygame
from threading import Thread
import os
from site1 import parse
H = 512
W = 640

level = 0

pygame.mixer.pre_init(44100, -16, 1, H)

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
color = {'B':W//4 - W //8,'G':W*2//4 - W //8,'Y':W*3//4 - W //8,'R':W*4//4 - W //8}
colors = {'B':(0,0,255),'G':(0,255,0),'Y':(255,255,0),'R':(255,0,0)}
fps = 60
clock = pygame.time.Clock()
ball = pygame.image.load('1.png')
sound1 = pygame.mixer.Sound("./hitsound.wav")
# pygame.mouse.set_visible(False)


def music_play():
    sound1 = pygame.mixer.Sound("./blends.wav")
    pygame.mixer.find_channel(True).play(sound1)

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
        self.y = H
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
        # pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        self.screen.blit(ball, (self.x - self.r, self.y - self.r))

    def move(self):
        self.y += self.velocity

    def __del__(self):
        self.y = H
        self.color = (0,0,0)
        self.r = 0


def main():
    v = parse(level)
    combo = 0
    combo_counter = 0
    temp = 0
    notes = []
    sliders = []
    points = 0
    timer = 0
    timer_for_penalty = 0
    while True:
        screen = pygame.display.set_mode((W,H))

        draw_field(screen)

        points_temp = points

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.KEYUP:
                # flag = False
                if i.key == pygame.K_4:
                    xtemp = W//4 - W //8
                elif i.key == pygame.K_5:
                    xtemp = W*2//4 - W //8
                elif i.key == pygame.K_6:
                    xtemp = W*3//4 - W //8
                elif i.key == pygame.K_7:
                    xtemp = W*4//4 - W //8
                elif i.key == pygame.K_w:
                    exit()
                else:
                    xtemp = -100


                for i in notes:
                    if i.y <  H*8//10 + 30 and i.y >  H*8//10 - 30 and i.x == xtemp:

                        pygame.mixer.find_channel(True).play(sound1)
                        points += 10 
                        if i.r != 0:
                            combo += 10
                        if combo >= 50: 
                            combo_counter += 1
                            combo = 0
                        timer_for_penalty = 0
                        i.__del__()


                for i in sliders:
                    i[1] += 1
                    if i[0].y < 465 and i[0].y + i[0].length > 445 and i[0].x == xtemp:
                        if i[1] >= 7:
                            i[1] = 0
                            points += 5
                            combo += 5 
                            timer_for_penalty = 0


            if points == points_temp:
                if timer_for_penalty >= 30:
                        points -= 5
                        timer_for_penalty = 0

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
            if i.y > H:
                if i.r != 0:
                    combo = 0
                    combo_counter = 0
                del i
                notes.pop(0)
                
            else:
                i.draw()
                i.move()

        for i in sliders:
            if i[0].y > H:
                i__del__()

            else:
                i[0].draw()
                i[0].move()

        textsurface = myfont.render(str(points), False, (255, 255, 255))
        screen.blit(textsurface,(50,10))

        textsurface = myfont.render(str(combo_counter), False, (255, 255, 255))
        screen.blit(textsurface,(50,80))

        pygame.display.flip()

        clock.tick(fps)

        temp += 1
        timer_for_penalty += 1


def draw_field(screen):
        pygame.display.set_caption("KekRythm")
        pygame.draw.rect(screen,(100, 100, 100), (0, 0, W, H))
        # pygame.draw.line(screen, (0, 0, 0), (0, 455), (W, 455), 1)
        pygame.draw.line(screen, (0, 0, 255), (W // 4 - W //8, 0), (W // 4 - W //8, H), 3)
        pygame.draw.line(screen, (0, 255, 0), (W // 2 - W //8, 0), (W // 2 - W // 8, H), 3)
        pygame.draw.line(screen, (255, 255, 0), (W * 3 // 4 - W //8, 0), (W * 3 // 4 - W //8, H), 3)
        pygame.draw.line(screen, (255, 0, 0), (W - W //8, 0), (W - W //8, H), 3)

        pygame.draw.circle(screen, (255, 255, 255), (W // 4 - W //8, H*8//10), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (128, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (W * 2// 4 - W //8, H*8//10), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (256, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (W * 3 // 4 - W //8, H*8//10), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (384, 455), 15)
        pygame.draw.circle(screen, (255, 255, 255), (W  - W //8,  H*8//10), 15, 1)
        # pygame.draw.circle(screen, (0, 0, 0), (H, 455), 15)



def fake_main():
    polling_thread = Thread(target = main)
    spam_thread = Thread(target = music_play)
    polling_thread.start()
    spam_thread.start()
    # music = pygame.mixer.music.load('./music.mp3')
    # pygame.mixer.music.play()


def menu():
    screen = pygame.display.set_mode((W, H))
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
                            level = 0
                        if selected == "stage 2":
                            pass  ## TODO: Карту №2
                        if selected == "stage 3":
                            pass  ## TODO: Карту №3
                        if selected == "quit":
                            pygame.quit()
                            quit()
                        pygame.display.quit()
                        return
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
            screen.blit(title, (W / 2 - (title_rect[2] / 2), 80))
            screen.blit(text_stage_1, (W / 2 - (stage_1_rect[2] / 2), 200))
            screen.blit(text_stage_2, (W / 2 - (stage_1_rect[2] / 2), 260))
            screen.blit(text_stage_3, (W / 2 - (stage_1_rect[2] / 2), 320))
            screen.blit(text_quit, (W / 2 - (quit_rect[2] / 2), 380))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
    main_menu()


if __name__ == "__main__":
    # os.system('python3 music_play.py')
    menu()
    fake_main()
