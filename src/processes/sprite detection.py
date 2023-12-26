import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *

class Sheldon(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = transform.scale(image.load('smallorangefish.png').convert(),(230,310))
        self.rect = self.image.get_rect()

class Rake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = transform.scale(image.load('salmon.png').convert(),(230,310))
        self.rect = self.image.get_rect()

class Sprite_Mouse_Location(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,1,1)
        print(self.rect)

pygame.init()
window = display.set_mode( (800,600) )
sheldon = Sheldon()
sheldon.rect = (10,10)
all_sprites = Group(sheldon)
rake = Rake()
rake.rect = (400,250)
all_sprites.add(rake)
x,y = pygame.mouse.get_pos()
mouse_sprite = Sprite_Mouse_Location(x,y)
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYUP and event.key == K_ESCAPE :
            pygame.quit()

        elif event.type == MOUSEMOTION :
            for s in all_sprites : 
                if pygame.sprite.collide_rect(s,mouse_sprite):
                    print("hit")

    window.fill( (0,0,0) )
    all_sprites.update()
    all_sprites.draw(window)
    display.update()