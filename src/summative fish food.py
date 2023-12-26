import pygame
from pygame import *
import random
import os

#initilization
init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
pygame.display.set_caption('coral compsci summative')
info = display.Info()
WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = display.set_mode(SIZE)

#COLOURS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,200)
WHITE= (255,255,255)
BLACK= (0,0,0)

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

Font = pygame.font.SysFont("freesansbold.ttf", 35)
HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK) #zero-pad hours to 2 digits
HourFontR=HourFont.get_rect()
HourFontR.center=(60,20)
#Minute
MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, BLACK) #zero-pad minutes to 2 digits
MinuteFontR=MinuteFont.get_rect()
MinuteFontR.center=(170,20)
#Second
SecondFont = Font.render("Second:{0:02}".format(Second),1, BLACK) #zero-pad seconds to 2 digits
SecondFontR=SecondFont.get_rect()
SecondFontR.center=(300,20)


foodCounter = 10
foodpoints = 0
NEWFOOD = 40
FOODSIZE = 20

player=Rect(300, 100, 50, 50)
foods=[]


computers=[]
comp_pos=[]
comp_list=[]

phones=[]


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

image= pygame.image.load('coralbackround.png')


def col_check(x,y,w,h,x2,y2,w2,h2):
        if (x < (x2 + w2) and (x + w) > x2 and y < (y2 + h2) and (h + y) > y2): 
                foods.remove(food)
                
def comp_fall(comp_list):
        delay=random.random()
        if len(comp_list) < 10 and delay < 0:
                comp_x = random.randint(o, WIDTH-50)
                comp_y=0
                comp_list.append([comp_x, comp_y])
        
def comp_draw(comp_list):
        for comp_pos in comp_list:
                pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], 50, 50))
                
        #def computer_positions(comp_list):
                #print("ok")
                
 
def ewasteee():
        for wa in range(0,900,10):
                place=random.randint(50,600)
                place2=random.randint(50,400) 
                place3=random.randint(250,600)
                place4=random.randint(150,300)
                pygame.draw.rect(screen,(0,0,70),(place,wa,50,50)) 
                pygame.draw.rect(screen,(0,0,170),(place2,wa,50,50)) 
                pygame.draw.rect(screen,(0,10,70),(place3,wa,50,50)) 
                pygame.draw.rect(screen,(10,0,70),(place4,wa,50,50)) 
        
               
def drawScreen(xlocation, ylocation):
        draw.rect(screen, (150,255,255), (0, 0, WIDTH, HEIGHT))
        #screen.fill(WHITE)
        screen.blit(image,(0,70))        
        
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
                ylocation+=4
                player=draw.rect(screen, GREEN, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))
        if MOVABLE==False:
                player=draw.rect(screen, RED, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))           
                #draw.circle(screen, RED, (xlocation, ylocation), 10)
        for i in range(len(foods)):
                pygame.draw.rect(screen, BLUE, foods[i]) 
        for food in foods:
                if player.colliderect(food):
                        foods.remove(food)
                        #foodpoints+=1
                               
        SecondFont = Font.render("Second:{0:02}".format(Second),1, BLACK)
        screen.blit(SecondFont, SecondFontR)
        MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, BLACK)
        screen.blit(MinuteFont, MinuteFontR)
        HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK)
        screen.blit(HourFont, HourFontR) 
        #ewasteee()

 

        #pygame.display.update()        
        display.flip()


def ewaste():
        for wa in range(0,900,10):
                place=random.randint(50,600)
                place2=random.randint(50,400) 
                place3=random.randint(250,600)
                place4=random.randint(150,300)
  
                #screen.blit(orangefish,(place3,count))
                #screen.blit(greenfish,(place,count))
                #screen.blit(pufferfish,(place4,count))
                pygame.draw.rect(screen,(0,0,70),(place4,wa,50,50))
                #fishpos1=[count,place]
                #screen.blit(salmon,(count,place2))
                #fishpos2=[count,place2]                
        
        
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
                        foodCounter+=1 

                        
                        
                elif MOUSEMOTION == False: 
                        #foodCounter = 0
                        #if Second%2==0:
                        foods.append(Rect(random.randint(0, WIDTH-FOODSIZE), random.randint(0, HEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))
                            # Draw the white background onto the surface.
                        #screen.fill(BLUE)
                          # Move the player.
                          
                if moveRIGHT == True and x>0:
                        x-=5
                if moveLEFT == True and x<WIDTH:
                        x+=5 
                if moveUP == True and y<HEIGHT-30:
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
                        if y>HEIGHT:
                                x,y=x,y
                        else:
                                x=x
                                y+=4                        
                if Second%10==0:
                        MOVABLE=True
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [True, True, True, True]    
                if Second%10==5:
                        MOVABLE=False
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [False, False, False, False]
                        
  
                drawScreen(x,y)
#for wa in range(0,900,10):
        #place=random.randint(50,600)
        #place2=random.randint(50,400) 
        #place3=random.randint(250,600)
        #place4=random.randint(150,300)
        #pygame.draw.rect(screen,(0,0,70),(place,wa,50,50)) 
        #pygame.draw.rect(screen,(0,0,170),(place2,wa,50,50)) 
        #pygame.draw.rect(screen,(0,10,70),(place3,wa,50,50)) 
        #pygame.draw.rect(screen,(10,0,70),(place4,wa,50,50)) 
                
                #display.update()   
                display.flip()
                Clock.tick(60)  
                

quit() 