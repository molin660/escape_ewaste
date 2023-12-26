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
ALIVE=True


def drawScreen(xlocation, ylocation):
        draw.rect(screen, BLUE, (0, 0, WIDTH, HEIGHT))
        if ALIVE==True:
                draw.rect(screen, GREEN, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))
        if ALIVE==False:
                draw.rect(screen, RED, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))                
        #draw.circle(screen, RED, (xlocation, ylocation), 10)
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
                if ALIVE==True:
                        if evnt.type == KEYDOWN:
                                if evnt.key == K_LEFT:
                                        moveLEFT = True
                                        moveRIGHT = False
                                if evnt.key == K_RIGHT:
                                        moveRIGHT = True
                                        moveLEFT = False
                                if evnt.key == K_DOWN:
                                        moveDOWN = True 
                                        moveUP = False
                                if evnt.key == K_UP:
                                        moveUP = True 
                                        moveDOWN = False
                            
                        if evnt.type == KEYUP:
                                if evnt.key == K_LEFT:
                                        moveLEFT = False
                                if evnt.key == K_RIGHT:
                                        moveRIGHT = False
                                if evnt.key == K_DOWN:
                                        moveDOWN = False 
                                if evnt.key == K_UP:
                                        moveUP = False                
                            
                if moveLEFT == True:
                        x-=10
                if moveRIGHT == True:
                        x+=10
                if moveDOWN == True:
                        y+=10
                if moveUP == True:
                        y-=10
                #if evnt.type == MOUSEBUTTONUP:
                        #foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
                        #foodCounter += 1                
                #if foodCounter >= NEWFOOD:
                        #foodCounter = 0
                        #foods.append(pygame.Rect(random.randint(0, WIDTH-FOODSIZE), random.randint(0, HEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))
                            ## Draw the white background onto the surface.
                        #screen.fill(WHITE)
                          ## Move the player.
                #if moveDOWN and player.bottom < WINDOWHEIGHT:
                        #player.top += MOVESPEED
                #if moveUP and player.top > 0:
                        #player.top -= MOVESPEED
                #if moveLEFT and player.left > 0:
                        #player.left -= MOVESPEED
                #if moveRIGHT and player.right < WINDOWWIDTH:
                        #player.right += MOVESPEED
                  ## Check whether the player has intersected with any food squares.
                #for food in foods[:]:
                        #if player.colliderect(food):
                                #foods.remove(food)
                  ## Draw the food.
                #for i in range(len(foods)):
                        #Rect(screen, GREEN, foods[i])
                # Draw the window onto the screen.
                display.update()                        
                        
                        
                        
                        
                if ALIVE==False:
                        x=x
                        y=y
                drawScreen(x,y)
                display.flip()
                Clock.tick(60)
                if Second%10==0:
                        ALIVE=True
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [True, True, True, True]    
                if Second%10==5:
                        ALIVE=False
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [False, False, False, False]

quit()