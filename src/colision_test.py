#from pygame import *
#init()
#RED = (255, 0, 0)
#BLACK = (0,0,0)
#info = display.Info()
#width = 500
#height = 300
#SIZE = (width, height)
#screen = display.set_mode(SIZE)
## function that draws everything we need onto the screen
#def drawScreen(location):
    #draw.rect(screen, BLACK, (0, 0, width, height))
    #draw.circle(screen, RED, (location, height - 100), 10)
    #display.flip()
#running = True
#x = width//2

#while running:
    #for evnt in event.get():
        #if evnt.type == QUIT:
            #running = False
        #if evnt.type == KEYDOWN:
            #keys = key.get_pressed()
            #if keys[K_RIGHT]:
                #x = x + 5
            #if keys[K_LEFT]:
                #x = x - 5
    #drawScreen(x)
    #display.flip()
#quit()


#from pygame import *
#init()
#RED = (255, 0, 0)
#BLACK = (0,0,0)
#info = display.Info()
#width = 500
#height = 300
#SIZE = (width, height)
#screen = display.set_mode(SIZE)
##some game states
#KEY_RIGHT = False
#KEY_LEFT = False
#def drawScreen(location):
    #draw.rect(screen, BLACK, (0, 0, width, height))
    #draw.circle(screen, RED, (location, height - 100), 10)
    #display.flip()
#running = True
#x = width//2
#while running:
    #for evnt in event.get():
        #if evnt.type == QUIT:
            #running = False
            #if evnt.type == KEYDOWN:
                #if evnt.key == K_LEFT:
                    #KEY_LEFT = True

                #if evnt.key == K_RIGHT:
                    #KEY_RIGHT = True
                #if evnt.type == KEYUP:
                    #if evnt.key == K_LEFT:
                        #KEY_LEFT = False
                    #if evnt.key == K_RIGHT:
                        #KEY_RIGHT = False
    #if KEY_LEFT == True:
        #x = x - 1
    #if KEY_RIGHT == True:
        #x = x + 1
    #drawScreen(x)
    #display.flip()
#quit()
