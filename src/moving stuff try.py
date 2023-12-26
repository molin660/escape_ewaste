import pygame
from pygame import *
import random
init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,200)
WHITE= (255,255,255)
BLACK= (0,0,0)
info = display.Info()
WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = display.set_mode(SIZE)#,FULLSCREEN)
#some game states
moveRIGHT = False
moveLEFT = False
moveDOWN = False
moveUP = False



Time = 0
Second = 0 
Minute = 0
Hour = 0
counter= 0

foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20

player=Rect(300, 100, 50, 50)
foods=[]
#Clock = time.Clock()
#CLOCKTICK = USEREVENT+1
#time.set_timer(CLOCKTICK, 1000)

orangefish=image.load('smallorangefish.png')
player =Rect(300, 100, 50, 50)
for a in range(10):
        foods.append(Rect(random.randint(0, WIDTH - FOODSIZE), random.randint(0, HEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
SPEED=5
MOVABLE=True
ALIVE=True

def col_check(x,y,w,h,x2,y2,w2,h2):
        if (x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2): 
                foods.remove(food)
        
        
def drawScreen(xlocation, ylocation):
        draw.rect(screen, BLUE, (0, 0, WIDTH, HEIGHT))
        
        #if evnt.type == MOUSEBUTTONUP:
                #foods.append(Rect(evnt.pos[0], evnt.pos[1], FOODSIZE, FOODSIZE))
                #foodCounter += 1          
        #if foodCounter >= NEWFOOD:
                #foodCounter = 0
                #foods.append(Rect(random.randint(0, WIDTH-FOODSIZE), random.randint(0, HEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))        
                
        #for i in range(len(foods)):
                #pygame.draw.rect(screen, GREEN, foods[i]) 
        #for food in foods:
                #if player.colliderect(food):
                        #foods.remove(food)        

        if MOVABLE==True:
                player=draw.rect(screen, GREEN, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))
        if MOVABLE==False:
                player=draw.rect(screen, RED, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))           
                #draw.circle(screen, RED, (xlocation, ylocation), 10)
        for i in range(len(foods)):
                pygame.draw.rect(screen, GREEN, foods[i]) 
        for food in foods:
                if player.colliderect(food):
                        foods.remove(food)      
        display.flip()
        
        
Clock = time.Clock()
CLOCKTICK = USEREVENT+1
time.set_timer(CLOCKTICK, 1000)

running = True
x = WIDTH//2
y = HEIGHT//2

while running:
        for evnt in event.get():
                if evnt.type == QUIT or evnt.type == KEYUP and evnt.key == K_ESCAPE:
                        running = False
                if evnt.type == CLOCKTICK:
                        Second+=1
                        if Second == 60:
                                Minute+=1
                                Second=0
                        if Minute==60: 
                                Hour+=1
                                Minute=0
                if MOVABLE==True:
                        if evnt.type == KEYDOWN:
                                if evnt.key == K_LEFT:
                                        moveRIGHT = True
                                        moveLEFT = False
                                if evnt.key == K_RIGHT:
                                        moveLEFT = True
                                        moveRIGHT = False
                                if evnt.key == K_DOWN:
                                        moveUP = True 
                                        moveDOWN = False
                                if evnt.key == K_UP:
                                        moveDOWN = True 
                                        moveUP = False
                            
                        if evnt.type == KEYUP:
                                if evnt.key == K_LEFT:
                                        moveLEFT = False
                                if evnt.key == K_RIGHT:
                                        moveRIGHT = False
                                if evnt.key == K_DOWN:
                                        moveDOWN = False 
                                if evnt.key == K_UP:
                                        moveUP = False                
                        
                        
                        
                if evnt.type == MOUSEBUTTONDOWN:
                        foods.append(Rect(evnt.pos[0], evnt.pos[1], FOODSIZE, FOODSIZE))
                        foodCounter += 1     
                        
                        
                if evnt.type != MOUSEBUTTONDOWN and MOUSEMOTION==False:
                        #foodCounter = 0
                        #if Second%3==0:
                        foods.append(Rect(random.randint(0, WIDTH-FOODSIZE), random.randint(0, HEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))
                            # Draw the white background onto the surface.
                        #screen.fill(BLUE)
                          # Move the player.
                          
                if moveRIGHT == True and x>0:
                        x-=5
                if moveLEFT == True and x<WIDTH:
                        x+=5 
                if moveUP == True and y<HEIGHT:
                        y+=5
                if moveDOWN == True and y>0:
                        y-=5   
                        
                #if moveDOWN and player.bottom < WINDOWHEIGHT:
                        #player.top += MOVESPEED
                #if moveUP and player.top > 0:
                        #player.top -= MOVESPEED
                #if moveLEFT and player.left > 0:
                        #player.left -= MOVESPEED
                #if moveRIGHT and player.right < WINDOWWIDTH:
                        #player.right += MOVESPEED
                        
                  ## Check whether the player has intersected with any food squares.
                #for food in foods:
                        #if player.colliderect(food):
                                #foods.remove(food)
                #for i in range(len(foods)):
                        #pygame.draw.rect(screen, GREEN, foods[i])        
                  ### Draw the food.
                ##Draw the window onto the screen.                   
                        
                                  
                        
                if MOVABLE==False:
                        x=x
                        y=y
                        
                if Second%10==0:
                        MOVABLE=True
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [True, True, True, True]    
                if Second%10==5:
                        MOVABLE=False
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [False, False, False, False]
  
                drawScreen(x,y)
                #display.update()   
                display.flip()
                Clock.tick(60)                        

quit() 