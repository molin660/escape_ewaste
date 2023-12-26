import pygame
import random
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [700, 600]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("HELP")
 
# Create an empty array
waste_list = []
indicators = []
 
def getmouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)


# Loop 50 times and add a waste flake in a random x,y position
for i in range(5):
    x = random.randint(0, 800)
    y = random.randint(0, 700)
    waste_list.append([x, y])
    for l in range(len(waste_list)):
        indicators.append(pygame.Rect(((waste_list[l][0]),(waste_list[l][1]),50,50)))
    indicators=indicators[-5: ]

print(waste_list)
print(indicators)

clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.

def waste(screen, mx, my):
    
      # Set the screen background
    screen.fill(BLACK)
    
      # Process each waste flake in the list
    for s in range(len(waste_list)):
        pygame.draw.rect(screen, WHITE, ((waste_list[s][0]), (waste_list[s][1]), 50, 50))
        #pygame.draw.rect(screen, BLACK, ((waste_list[i][0])+5,(waste_list[i][1])+5,20,10))
  
        # Move the waste flake down one pixel
        waste_list[s][1] += 1
    
        # If the waste flake has moved off the bottom of the screen
        if waste_list[s][1] > 600:
            # Reset it just above the top
            y = random.randint(-50, -10)
            waste_list[s][1] = y
            # Give it a new x position
            x = random.randint(0, 400)
            waste_list[s][0] = x
            for ind in range(len(waste_list)): 
                if mx>waste_list[ind][0] and mx<=((waste_list[ind][1])+50) and my>waste_list[ind][1] and my<=((waste_list[ind][1])+50) and pygame.mouse.get_pressed()[0]==1:
    #if mouse_x > object[pos_x] and mouse_x <= object[pos_x] + object[length] and mouse_y > object[pos_y] and mouse_y <= object[pos_y] + object[width] and mouse_press == 1:
                #if indicators[ind].collidepoint(mx,my) and pygame.mouse.get_pressed()[0]==1:
                    pygame.draw.rect(screen, WHITE, indicators[ind], 0)
                    pygame.display.set_caption("Collision Detected!")     
                else:
                    pygame.draw.rect(screen, (255,0,0), indicators[ind], 0)
                    pygame.display.set_caption("No collision detected")            
            
done=False
while not done: 
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
        # Go ahead and update the screen with what we've drawn.
        mx, my, mb = getmouse()
        waste(screen, mx, my)
        pygame.display.flip()
        #clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.




    
pygame.quit()

#print(waste_list)