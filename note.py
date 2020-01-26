import pygame


class note(pygame.sprite.Sprite):
    def __init__(self, x, surf, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect((x, 512))
        self.speed = speed
        self.x=x
        self.y=512


    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:

            self.kill()


# class note:
#     time_start=0
#     velocity=0
#     ttl=0
#     width=30
#     height=30
#
#     def  __init__(self,surface,number,x,img):
    #     #создание ноты
    #     self.surf = surface
    #     self.number=number
    #     self.x=x
    #     self.y=512
    #     self.img=img
    #
    # def spawn(self,x,img):
    #     note.x=x
    #     noteimg = pygame.image.load(img)
    #     note.rect = noteimg.get_rect(note.x,512,30,30)
    #
    # def move(self):





