import pygame

pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)
mx, my = 0,0
def drawScene(screen):
    red = 255, 0, 0
    if pygame.mouse.get_pressed()[0]==1:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(screen,red,(mx,my), 10)
running = True
myClock = pygame.time.Clock()
while running:
    for evnt in pygame.event.get(): # checks all events that happen
        if evnt.type == pygame.QUIT:
            running = False
    drawScene(screen)
    pygame.display.flip()
    myClock.tick(60)
pygame.quit()