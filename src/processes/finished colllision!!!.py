import pygame
from pygame import *
import random
import os

#Initilization of pygame window 
init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)

#Displays the name of the game 
pygame.display.set_caption('coral compsci summative')
info = display.Info()

#Setting screen size
WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = display.set_mode(SIZE)

#CONSTANT COLOURS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,200)
WHITE= (255,255,255)
BLACK= (0,0,0)

#Backround
image= pygame.image.load("\images\coralbackround.png")

#The player is an orange fish 
orangefish=pygame.image.load('smallorangefish.png')

#Some initial game states
moveRIGHT = False
moveLEFT = False
moveDOWN = False
moveUP = False

#Time used to stop players from being able to move every so often
Clock = time.Clock()
CLOCKTICK = USEREVENT+1
time.set_timer(CLOCKTICK, 1000)
#The time starts at zero 
Time = 0
Second = 0 
Minute = 0
Hour = 0



foodCounter = 10
foodpoints = 0
NEWFOOD = 40
FOODSIZE = 20

FISHSPEED=5

foods=[]


computers=[]
comp_pos=[random.randint(0,WIDTH-50), 0]
comp_list=[comp_pos]
score=0
phones=[]

#Font for texts
Font = pygame.font.SysFont("freesansbold.ttf", 35)

#Hours
HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK) #zero-pad hours to 2 digits
HourFontR=HourFont.get_rect()
HourFontR.center=(60,20)
#Minutes
MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, BLACK) #zero-pad minutes to 2 digits
MinuteFontR=MinuteFont.get_rect()
MinuteFontR.center=(170,20)
#Seconds
SecondFont = Font.render("Second:{0:02}".format(Second),1, BLACK) #zero-pad seconds to 2 digits
SecondFontR=SecondFont.get_rect()
SecondFontR.center=(300,20)

#PointsFont = Font.render("Points: {000}".format(foodpoints),1, BLACK)
#PointsFontR=PointsFont.get_rect()
#PointsRect.center = (60,60)


def time(): #to display the time at the top left corner 
        SecondFont = Font.render("Second:{0:02}".format(Second), 1, BLACK) #zero-pad hours to 2 digits
        screen.blit(SecondFont, SecondFontR)
        MinuteFont = Font.render("Minute:{0:02}".format(Minute), 1, BLACK) #zero-pad minutes to 2 digits
        screen.blit(MinuteFont, MinuteFontR)
        HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK)#zero-pad seconds to 2 digits
        #Pointsfont = Font.render("Points: {000}".format(foodpoints), 1, BLACK)
        #screen.blit(PointsFont, PointsFontR)
        






player = Rect(WIDTH//2, HEIGHT//2, 50, 50)
for a in range(10):
        foods.append(Rect(random.randint(0, WIDTH - FOODSIZE), random.randint(0, HEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
SPEED=5
MOVABLE=True
ALIVE=True


def getmouse(): 
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()[0]
        return (mx, my, mb)
        
waste_list = []
indicators = []
#for b in Minute:
        #if Minute:
for i in range(5):
        x = random.randint(0, 650)
        y = random.randint(0, 300)
        waste_list.append([x, y])
        
def waste(screen, mx, my):
        for s in range(len(waste_list)):
                indicators=[]
                pygame.draw.rect(screen, WHITE, ((waste_list[s][0]), (waste_list[s][1]), 50, 50))
                indicators.append(pygame.Rect(((waste_list[s][0]),(waste_list[s][1]),50,50)))
                #for b in range (len(Minute)):
                global Minute
                indicators=indicators[-5: ]        
                #pygame.draw.rect(screen, BLACK, ((waste_list[s][0])+5,(waste_list[s][1])+5,40,40))
            
                # Move the ewaste down one to three pixel(s)
                waste_list[s][1] += random.randint(0,3)
            
            # If the waste flake has moved off the bottom of the screen
                if waste_list[s][1] > 600:
                    # Resets the y position    
                        y2 = random.randint(-50, -10)
                        waste_list[s][1] = y2
                    # Give it a new x position
                        x2 = random.randint(0, 650)
                        waste_list[s][0] = x2 
                    # Replaces the old point with the new one
                        waste_list.remove(waste_list[s])
                        waste_list.append([x2, y2])
                    
                    
        for ind in range(len(indicators)):
                if indicators[ind].collidepoint(mx,my):
                        pygame.draw.rect(screen, (255,255,0), indicators[ind], 0)
                        pygame.display.set_caption("Collision Detected!")
                        if pygame.mouse.get_pressed()[0]==1:
                                clickcheck=True
                                if Second%3==0:
                                        pygame.draw.rect(screen, (0,255,255), indicators[ind], 0)
                                        foods.append(Rect(mx, my, FOODSIZE, FOODSIZE))
                                        global foodCounter
                                        foodCounter+=1
                        
                else:
                        pygame.draw.rect(screen, WHITE, ((waste_list[ind][0]), (waste_list[ind][1]), 50, 50))
                        pygame.display.set_caption("No collision detected")          
     
               
def drawScreen(xlocation, ylocation):
        # Displaying the coral reef backround
        draw.rect(screen, (150,255,255), (0, 0, WIDTH, HEIGHT))
        screen.blit(image,(0,70))


        if MOVABLE==True:
                ylocation+=4
                player=draw.rect(screen, GREEN, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))
        if MOVABLE==False:
                player=draw.rect(screen, RED, (xlocation-5, ylocation-5, 60, 30))
                screen.blit(orangefish,(xlocation,ylocation))   
        for i in range(len(foods)):
                pygame.draw.rect(screen, BLUE, foods[i])
        for ewaste in waste_list:
                if player.colliderect(ewaste[0],ewaste[1],50,50): 
                        pygame.draw.circle(screen,(7,200,78), (300,200), 60)
                        #quit()
        for food in foods:
                if player.colliderect(food):
                        foods.remove(food)
                        global foodCounter
                        foodCounter-=1
                        global foodpoints
                        foodpoints+=1
                               
        #SecondFont = Font.render("Second:{0:02}".format(Second),1, BLACK)
        #screen.blit(SecondFont, SecondFontR)
        #MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, BLACK)
        #screen.blit(MinuteFont, MinuteFontR)
        #HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK)
        time()
        screen.blit(HourFont, HourFontR) 
        mx,my,mb = getmouse()
        waste(screen, mx, my)
        #ewasteee()
        #comp_draw(comp_list)

 

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
                        
                        
                        
                #if evnt.type == MOUSEBUTTONDOWN:
                        #foods.append(Rect(evnt.pos[0], evnt.pos[1], FOODSIZE, FOODSIZE))
                        #foodCounter+=1 

        
                elif MOUSEMOTION == False:
                        foods.append(Rect(random.randint(0, WIDTH-FOODSIZE), random.randint(0, HEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))

                          
                if moveRIGHT == True and x>0:
                        x-=FISHSPEED
                if moveLEFT == True and x<WIDTH:
                        x+=FISHSPEED
                if moveUP == True and y<HEIGHT-30: 
                        y+=FISHSPEED

                if moveDOWN == True and y>0:
                        y-=FISHSPEED            
        
                #if MOVABLE==False:
                        #if y>HEIGHT:
                                #x,y=x,y
                        #else:
                                #x=x 
                                #y+=4                        
                if Second%10==0:
                        FISHSPEED=5
                        MOVABLE=True
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [True, True, True, True]    
                if Second>10 and Second%15==0 and Second%10!=0 or Second>=55:
                        MOVABLE=False
                        FISHSPEED=1
                mx,my,mb = getmouse()
                        
                        
        drawScreen(x,y)
        display.update()   
        display.flip()
        Clock.tick(60)  
                

quit()

print(waste_list)
print(indicators)
print(foods)
print(foodCounter)
print(foodpoints)
print(Minute)