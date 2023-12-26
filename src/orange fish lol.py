import random 
import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

#info=display.Info()
pygame.init() #initializing pygame 
SIZE= (1000, 700) #SIZE= (x,y)
screen= pygame.display.set_mode(SIZE)
BLACK=(0,0,0)
#for count in range (0, 900, 10):
    #screen.fill(BLACK)
    #if count>900:
        #count in range(0,900,-10)
        #pygame.draw.circle(screen, (153, 240, 230), (count, 250), 75)
        
        
surface = pygame.display.set_mode((800,600))
orangefish= pygame.image.load('pufferfish.png')
salmon= pygame.image.load('smallorangefish.png')
#greenfish= pygame.image.load('greenfish.png')
##make the fish and graphics lol
##try to add them all into the actual backround with the clock
##if you have time attempt the collision detection
for count in range (0, 900, 10):
    screen.fill(BLACK)
    surface.blit(orangefish,(count,70))
    pygame.display.update()
    pygame.time.wait(random.randint(100,600))

for count2 in range (0, 900, 10):
    screen.fill(BLACK)
    surface.blit(salmon,(count2,70))
    pygame.display.update()
    pygame.time.wait(random.randint(100,600))
    
#orangefish= pygame.image.load("transparent orange fish.png")
#screen.blit(orangefish, pygame.Rect(100,100,105,78))

#pygame.display.flip()