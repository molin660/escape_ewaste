#Name:Molin Li
#Date:December, 2019
#Class:ICS3U1-04
#Description: Summative lol

#importing all built-in programs necessary
import random 
import pygame
import math
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

#info=display.Info()
pygame.init() #initializing pygame 
SIZE= (1000, 700) #SIZE= (x,y)
screen= pygame.display.set_mode(SIZE)


pygame.init()
#SIZE= (x,y)
SIZE= (800, 600)
screen= pygame.display.set_mode(SIZE)
BLACK=(0,0,0)
screen.fill(BLACK)
for count in range (0, 900, 10):
    screen.fill(BLACK)
    if count>900:
        count in range(0,900,-10)
        pygame.draw.circle(screen, (153, 240, 230), (count, 250), 75)
    if count<10:
        
        pygame.display.flip()
        pygame.time.wait(150)
pygame.quit()

