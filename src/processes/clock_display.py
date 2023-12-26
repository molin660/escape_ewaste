import pygame

pygame.init()

#Screen
size = width, height = 800, 600 #Make sure background image is same size
screen = pygame.display.set_mode(size)

done = False

#Time Info
Time = 0
Second = 0
Minute = 0
Hour = 0
counter=0

surface = pygame.display.set_mode((800,600))
image= pygame.image.load('coralbackround.png')

surface.blit(image,(0,70))
pygame.display.update()

#Colour
Black = (0,0,0)
White = (255, 255, 255)

#Fonts
Font = pygame.font.SysFont("freesansbold.ttf", 35)

#Hour
HourFont = Font.render("Hour:{0:02}".format(Hour),1, Black) #zero-pad hours to 2 digits
HourFontR=HourFont.get_rect()
HourFontR.center=(60,20)
#Minute
MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, Black) #zero-pad minutes to 2 digits
MinuteFontR=MinuteFont.get_rect()
MinuteFontR.center=(170,20)
#Second
SecondFont = Font.render("Second:{0:02}".format(Second),1, Black) #zero-pad seconds to 2 digits
SecondFontR=SecondFont.get_rect()
SecondFontR.center=(300,20)

Clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # fired once every second

screen.fill(White)
while done==False:
    #checks if user would like to exit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True #when the "x" is clicked, the whole window closes
            
        if event.type == CLOCKTICK: # counts up the clock
            #Timer
            Second=Second+1
            if Second == 60: #"if 1 minute has passed, add a minute to the "minutes counter" and reset the seconds
                Minute+=1
                Second=0
            if Minute==60: #"if 1 hour has passed, add an hour to the "hours counter" and reset the minutes (Extra, very hard to acheive)
                Hour+=1
                Minute=0
                
            # redraw time
            screen.fill(White)
            SecondFont = Font.render("Second:{0:02}".format(Second),1, Black)
            screen.blit(SecondFont, SecondFontR)
            MinuteFont = Font.render("Minute:{0:02}".format(Minute),1, Black)
            screen.blit(MinuteFont, MinuteFontR)
            HourFont = Font.render("Hour:{0:02}".format(Hour),1, Black)
            screen.blit(HourFont, HourFontR)

            pygame.display.flip()

    Clock.tick(60) #maximum of 60 frames per second (a minute)

pygame.quit()