#Name: Molin Li
#Date: December, 2019 - Jan, 2020
#Class: ICSU1-04
#Decription: This is my final summative task which is creating a video game 

#imports pythons built in functions
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
YELLOW=(255,255,0)
ORANGE=(250,170,0)
CYAN=(0,255,255)
GREY=(50,50,50)
HEALTHRED=(222,111,111)

#Loading the Backround that I drew in Paint 
image= pygame.image.load('coralbackround.png')
#Loading the Image for The player as an orange fish  
orangefish=pygame.image.load('leftorangefish.png')
orangefish2=pygame.image.load('rightorangefish.png')

title=pygame.image.load('title.png')
instructions=pygame.image.load('instructions.png')

############Some initial game states---------------------------------------------------------------------
#the original position of the player is centered in the screen
player = Rect(WIDTH//2, HEIGHT//2, 50, 50)

#loads title
titlepic = True

#loads instructions
starting = False

#allows the game loop to run
running = False

#initial x and y points 
x = WIDTH//2
y = HEIGHT//2

#does not move when starting
moveRIGHT = False
moveLEFT = False
moveDOWN = False
moveUP = False

#is able to move whenever player wants to start
MOVABLE=True
#is alive at the start
ALIVE=True
#faces left to start of with
direction='left'

#Time used to tell time and show, stops players from being able to move every so often
Clock = time.Clock()
CLOCKTICK = USEREVENT+1
time.set_timer(CLOCKTICK, 1000)

#The time starts at zero 
Second = 0 
Minute = 0
Hour = 0

#player starts off with 10 potential food pellets
foodCounter = 10
#starts off with 0 points 
foodpoints = 0
#the size of the food is constantly square 
FOODSIZE = 20
#list of food, they will be added later on
foods=[]
allpoints=[]

#Health starts off at 100 helath points 
FishHealth=100
#constant speed of mouvement from player 
FISHSPEED=5

#the e-waste can generate from 8-12 pieces 
wasteAmount=random.randint(8,12)
#these empty lists will be filled in with the coordinates of the e-waste later on (they are T.Vs)
waste_list = []
indicators = []

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

#the title starts first
while titlepic == True:
        screen.fill(WHITE)
        screen.blit(title,(0,0))      
        
        for event3 in event.get():
                if event3.type == KEYDOWN and event3.key == K_SPACE:
                        titlepic=False
                        starting=True
                        running=False
        display.flip()
#when player presses space, the instructions show                        
while starting == True:
        screen.blit(instructions,(0,0))
        pygame.draw.rect(screen, GREY, (390,340, 50, 50))
        pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), ((395,345,40,30)))
        pygame.draw.rect(screen, GREY, (500,260, 50, 50))
        pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), ((505,265,40,30)))
        pygame.draw.rect(screen, BLUE, (580,280,20,20))
        pygame.draw.rect(screen, BLUE, (620,310,20,20))
        for event2 in event.get():
#if they press space again, the game actually starts
                if event2.type == KEYDOWN and event2.key == K_SPACE:
                        titlepic=False
                        starting=False
                        running=True                                   
                if event2.type == QUIT or event2.type == KEYUP and event2.key == K_ESCAPE:
                        starting = False
                        running = False   
        display.flip()
        



def time(): #to display the time at the top left corner 
        SecondFont = Font.render("Second:{0:02}".format(Second), 1, BLACK) #zero-pad hours to 2 digits
        screen.blit(SecondFont, SecondFontR)
        MinuteFont = Font.render("Minute:{0:02}".format(Minute), 1, BLACK) #zero-pad minutes to 2 digits
        screen.blit(MinuteFont, MinuteFontR)
        HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK)#zero-pad seconds to 2 digits
        screen.blit(HourFont, HourFontR) 

def getmouse(): #constantly finds the mouse coordinates which will be used to click on the e-waste 
        mx, my = pygame.mouse.get_pos() 
        mb = pygame.mouse.get_pressed()[0]
        return (mx, my, mb)

#as mentioned before, the initial amount of food is ten, the loop will randomly generate the location of these ten pieces of food and add them to the list of all foods
for a in range(foodCounter):
        foods.append(Rect(random.randint(0, WIDTH - FOODSIZE), random.randint(0, HEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

#again, as mentioned previously, the amount of e-waste will be from 5-10 pieces, this loop will assign random initial values for them        
for i in range(wasteAmount):
        x = random.randint(0, WIDTH) #anywhere along the x-axis
        y = random.randint(0, 100) #starts near the top of the screen 
        waste_list.append([x, y]) #adds it to the list of e-waste positions

#to detect for collision and draw the actual T.Vs        
def waste(screen, mx, my):
        for s in range(len(waste_list)): #allocates indicator values, however, only one of the boxes can be indicated at a time
                indicators=[]
                pygame.draw.rect(screen, GREY, ((waste_list[s][0]), (waste_list[s][1]), 50, 50))
                pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), ((waste_list[s][0])+5,(waste_list[s][1])+5,40,30))
                indicators.append(pygame.Rect(((waste_list[s][0]),(waste_list[s][1]),50,50)))
                #global Minute
                indicators=indicators[-wasteAmount: ]        
            
                # Move the ewaste down one to three or six pixel(s)
                waste_list[s][1] += random.randint(0,3)
                
            # If the waste has moved off the bottom of the screen
                if waste_list[s][1] > 600:
                    # Resets the y position    
                        y2 = random.randint(-50, -10)
                        waste_list[s][1] = y2
                    # Give it a new x position
                        x2 = random.randint(0, WIDTH)
                        waste_list[s][0] = x2 
                    # Replaces the old point with the new one
                        waste_list.remove(waste_list[s])
                        waste_list.append([x2, y2])
                    
                    
        for ind in range(len(indicators)):
                #if the indicator collides with one of the mouse points, the T.V turns yellow to indicate that the player found the right one  
                if indicators[ind].collidepoint(mx,my):
                        pygame.draw.rect(screen, YELLOW, indicators[ind], 0)
                        #sets the window as the name "Collision Detected!" to show the player just incase they miss the yellow box
                        pygame.display.set_caption("Collision Detected!")
                        if pygame.mouse.get_pressed()[0]==1: #if they are within the range of the correct T.V
                                clickcheck=True
                                if Second%3==0: #AND they also press down on the mouse, every three seconds they will be able to generate a new food pellet in place of the e-waste
                                        pygame.draw.rect(screen, CYAN, indicators[ind], 0)
                                        pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),((indicators[ind][0])+5, (indicators[ind][1])+5,40,30))
                                        foods.append(Rect(mx, my, FOODSIZE, FOODSIZE))  #it is drawn and added to the list of foods   
                                        #the foodCounter counts how much food is on the screen, so, it will add another one
                                        global foodCounter
                                        foodCounter+=1
######_--------------------------------------------------------------                       
                else:
                        #(xx)=(waste_list[ind][0])
                        #(yy)=(waste_list[ind][1])
                        pygame.draw.rect(screen, GREY, ((waste_list[ind][0]), (waste_list[ind][1]), 50, 50))
                        pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), ((waste_list[s][0])+5,(waste_list[s][1])+5,40,30))
                        #pygame.display.set_caption("No collision detected")          
     
#draws the screen for playing purposes...               
def drawScreen(xlocation, ylocation, direction):
        # Displaying the coral reef backround
        draw.rect(screen, (150,255,255), (0, 0, WIDTH, HEIGHT))
        screen.blit(image,(0,70))

#animates the fish which is the player depending on its facing direction and ability to move (spawn points vary each time)
        if MOVABLE==True: #displays the green box to represent 'go' i.e the player is able to move around freely 
                player=draw.rect(screen, GREEN, (xlocation-5, ylocation-5, 60, 30))
                if direction=='right':
                        screen.blit(orangefish,(xlocation,ylocation))
                if direction=='left':
                        screen.blit(orangefish2,(xlocation,ylocation))
        if MOVABLE==False: #the player is stopped and can not move 
                player=draw.rect(screen, RED, (xlocation-5, ylocation-5, 60, 30)) 
                if direction=='right':               
                        screen.blit(orangefish,(xlocation,ylocation))   
                if direction=='left':                
                        screen.blit(orangefish2,(xlocation,ylocation))           
        ylocation+=4 #the constant gravity of the ocean 
        
#displays the food that is in the foods list
        for i in range(len(foods)):
                pygame.draw.rect(screen, BLUE, foods[i])
#detects for collision with the e-waste, if there is collision, the player will lose health and need to move away from it, there is also a first aid symbol in the corner to indicate the loss of health
        for ewaste in waste_list: 
                if player.colliderect(ewaste[0],ewaste[1],50,50): 
                        pygame.draw.circle(screen, HEALTHRED, (WIDTH,0), 160)
                        pygame.draw.rect(screen,WHITE, (WIDTH-50,70,20,50))
                        pygame.draw.rect(screen,WHITE, (WIDTH-70,85,60,20))
                        global FishHealth
                        FishHealth-=1
####################if the health reaches 0, it dies, and the game ends 
                if FishHealth==0:
                        ALIVE=False
                        running=False
                        quit()
                        #screen.fill(BLUE)
                        #screen.blit((font.SysFont("underlined Text",30)).render(("You got:  %i"%foodpoints),1,BLACK,ORANGE),Rect(580,40,20,20))
                        #display.flip()                        

                        #quit()
#checks for food collision, if there is, a point will be added to the score, it will gain a bit of health and then it will be removed from the foods list as it is no longer a piece of food
        for food in foods:
                if player.colliderect(food):
                        foods.remove(food)
                        global foodCounter
                        foodCounter-=1
                        global foodpoints
                        foodpoints+=1
                #because of bio-accumulation, sometimes, eating food from contaminated water decreases health 
                        FishHealth+=random.randint(-3,3)
                               
        time() #bringing back the time function to display the time
#shows the points in the top right corner highlighted in orange 
        screen.blit((font.SysFont("underlined Text",30)).render(("Score:  %i"%foodpoints),1,BLACK,ORANGE),Rect(580,10,20,20))
        screen.blit((font.SysFont("underlined Text",30)).render(("Health:  %i"%FishHealth),1,BLACK,ORANGE),Rect(580,40,20,20))
#gets the mouse positions for mouse collision detection
        mx,my,mb = getmouse()
#displays the e-waste 
        waste(screen, mx, my)
#flips the image to see
        #pygame.display.update()        
        #display.flip()



while running:
        for evnt in event.get(): #checking for events 
#if they player wants to exit, they can press the 'escape' button or the 'X' on the tab
                if evnt.type == QUIT or evnt.type == KEYUP and evnt.key == K_ESCAPE:
                        running = False
#allows for the time to progress
                if evnt.type == CLOCKTICK:
                        #with each second survived, the player receives 1 health point
                        Second+=1
                        FishHealth+=1
                        if Second == 60:
                                Minute+=1
                                Second=0
                        if Minute == 60: 
                                Hour+=1
                                Minute=0
#if the player has the right to move, they will be able to go up, down, left or right by pressing the corresponding keys on the keyboard  
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
                                        
#if the player presses the z on the keyboard, they will be teleported to another part of the screen, this could potentially save them or bring them closer to the e-waste  (risk/benefit) factor
                                if evnt.key == K_z:
                                        x=random.randint(10,WIDTH-50)
                                        y=random.randint(10,HEIGHT-50)                                        
#if nothing is pressed down, nobody moves                            
                        if evnt.type == KEYUP:
                                if evnt.key == K_LEFT:
                                        moveLEFT = False
                                if evnt.key == K_RIGHT:
                                        moveRIGHT = False
                                if evnt.key == K_DOWN:
                                        moveDOWN = False 
                                if evnt.key == K_UP:
                                        moveUP = False
                #elif MOUSEMOTION == False:
                        #foods.append(Rect(random.randint(0, WIDTH-FOODSIZE), random.randint(0, HEIGHT-FOODSIZE), FOODSIZE, FOODSIZE))

#if they press the respective keys and the player is still within the boundaries of the window, they will move 5 pixels in that direction                           
                if moveRIGHT == True and x>0:
                        x-=FISHSPEED
                        direction='right'
                if moveLEFT == True and x<WIDTH:
                        x+=FISHSPEED
                        direction='left'
                if moveUP == True and y<HEIGHT-30: 
                        y+=FISHSPEED
                if moveDOWN == True and y>0:
                        y-=FISHSPEED            
#at 15,45, and 55 seconds, for 5 seconds, the player is generally frozen in place and cannot move, otherwise, they can 
                if Second%10==0:
                        MOVABLE=True
                        [moveLEFT,moveRIGHT,moveUP,moveDOWN] = [True, True, True, True]    
                if Second>10 and Second%15==0 and Second%10!=0 or Second>=55:
                        MOVABLE=False
                        FISHSPEED=1
                #if Second==15:
                        #wasteAmount+=1
#gets the mouse positions 
                mx,my,mb = getmouse()
#actually draws the screen and continues with the clock                  
        drawScreen(x,y,direction)                   
        display.flip()   
        Clock.tick(60)
        
        if ALIVE==False:
                screen.fill(BLUE)
                screen.blit((font.SysFont("underlined Text",30)).render(("You got:  %i"%foodpoints),1,BLACK,ORANGE),Rect(580,40,20,20))
                display.flip()           
        
        
        def write_file(foodpoints):
                numFile= open('points.txt','w')
                for p in range(len(allpoints)):     
                        numFile.write(str(foodpoints[p]) + '\n')
                
        allpoints=[] 
        
        going=True
        content=open("points.txt","r")
        
        while going:
                text=content.readline()
                text=text.rstrip('\n') 
                if text=='':
                        going=False
                        break
                else:                      
                        allpoints += [int(text)]
        allpoints +=[int(foodpoints)]
numFile.close()
        
        
print(allpoints)
write(allpoints)
        

#while ALIVE==False:
        #screen.fill(BLUE)
        #display.flip()
        
#def write_file(foodpoints):
        #numFile= open('points.txt','w')
        #numFile.write(str(foodpoints) + '\n')
        
#allpoints=[] 

#going=True
#content=open('points.txt','r')

#while going:
        #text=content.readline()
        #if text=='':
                #going=False
        #else:
                #text.rstrip('\n')                                                
                #allpoints += [int(text)]
#allpoints +=[int(foodpoints)]


#print(allpoints)
#write(allpoints)

quit()

       
        
        
print(waste_list)
print(indicators)
print(foods)
print(foodCounter)
print(foodpoints)















