import pygame
import random

pygame.init()

#Screen
SIZE = width, height = 800, 500 #Make sure background image is same size
screen = pygame.display.set_mode(SIZE)

done = False

#Time Info
Time = 0
Second = 0
Minute = 0
Hour = 0
counter= 0

pygame.display.set_caption('coral compsci summative')

#Colour
BLACK = (0,0,0)
WHITE = (255, 255, 255)

#Fonts
Font = pygame.font.SysFont("freesansbold.ttf", 35)
screen = pygame.display.set_mode((700,600))
image= pygame.image.load('coralbackround.png')
screen.fill(WHITE)
screen.blit(image,(0,70))
pygame.display.update()


#orangefish= pygame.image.load('smallorangefish.png')

#for count in range (0, 900, 10):
    #place=random.randint(50,100)
    #place2=random.randint(50,100)                     
    #screen.fill(WHITE)
    #screen.blit(image,(0,70))    
    #screen.blit(orangefish,(count,place))

    #for l in range(50,100):
        #pygame.draw.rect(screen, BLACK, (place+l, l, place, place2),2)
    #pygame.display.update()
    #pygame.time.wait(random.randint(100,600))
    
#fish

#fishplaces=[fishpos1,fishpos2]
#ewaste=[]


#Hour
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

Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second

screen.blit(image,(0,70))
pygame.display.update()
while done==False:
    #checks if user would like to exit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True #when the "x" is clicked, the whole window closes
            
            #orangefish= pygame.image.load('smallorangefish.png')
            
            #for count in range (0, 900, 10):
                #place=random.randint(50,100)
                #place2=random.randint(50,100)    
                #screen.fill(WHITE)
                #screen.blit(image,(0,70))    
                #screen.blit(orangefish,(count,place))
            
                #for l in range(50,100):
                    #pygame.draw.rect(screen, BLACK, (place+l, l, place, place2),2)
                #pygame.display.update()
                #pygame.time.wait(random.randint(100,600))            
            
        if event.type == CLOCKTICK: # counts up the clock
            #Timer
            Second+=1
            if Second == 60: #"if 1 minute has passed, add a minute to the "minutes counter" and reset the seconds
                Minute+=1
                Second=0
            if Minute==60: #"if 1 hour has passed, add an hour to the "hours counter" and reset the minutes (Extra, very hard to acheive)
                Hour+=1
                Minute=0 
            # redraw time
            screen.fill(WHITE)
            screen.blit(image,(0,70))
            pygame.display.update()
            SecondFont = Font.render("Second:{0:02}".format(Second),1, BLACK)
            screen.blit(SecondFont, SecondFontR)
            MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, BLACK)
            screen.blit(MinuteFont, MinuteFontR)
            HourFont = Font.render("Hour:{0:02}".format(Hour),1, BLACK)
            screen.blit(HourFont, HourFontR)
            

            pygame.display.flip()

    Clock.tick(60) #maximum of 60 frames per second (a minute)



orangefish= pygame.image.load('smallorangefish.png')
salmon=pygame.image.load('salmon.png')
greenfish=pygame.image.load('greenfish.png')
pufferfish=pygame.image.load('pufferfish.png')



for count in range (0, 900, 10):
    place=random.randint(50,100)
    place2=random.randint(50,100) 
    place3=random.randint(50,100)
    place4=random.randint(150,200)
    screen.fill(WHITE)
    screen.blit(image,(0,100))    
    screen.blit(orangefish,(count,place3))
    screen.blit(greenfish,(count,place))
    screen.blit(pufferfish,(count,place4))
    fishpos1=[count,place]
    screen.blit(salmon,(count,place2))
    fishpos2=[count,place2]



    #for l in range(50,100,5):
        #pygame.draw.rect(screen, BLACK, (place+l, l, place, place2),2)
        #pygame.draw.rect(screen, (90,3,12), (place, l, place2, place),2)
        #pygame.draw.rect(screen, (4,15,80), (l, place, place2, place),2)
    pygame.display.update()
    pygame.time.wait(random.randint(100,600))
    
    


pygame.quit()