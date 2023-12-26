import pygame
import random
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [700, 600]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# Create an empty array
snow_list = []
 
def getmouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)


# Loop 50 times and add a snow flake in a random x,y position
for i in range(10):
    x = random.randint(0, 800)
    y = random.randint(0, 700)
    snow_list.append([x, y])

 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.

def snow(screen, mx, my):
    
      # Set the screen background
    screen.fill(BLACK)
    
      # Process each snow flake in the list
    for i in range(len(snow_list)):
    
          # Draw the snow flake
        pygame.draw.rect(screen, WHITE, ((snow_list[i][0]),(snow_list[i][1]),50,50))
        #pygame.draw.rect(screen, BLACK, ((snow_list[i][0])+5,(snow_list[i][1])+5,20,10))
  
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
  
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 600:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            snow_list[i][0] = x
done=False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
        # Go ahead and update the screen with what we've drawn.
        mx, my, mb = getmouse()
    snow(screen, mx, my)
    pygame.display.flip()
    clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.


pygame.quit()

print(snow_list)