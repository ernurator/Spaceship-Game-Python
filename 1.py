import pygame
#pylint: disable=no-member

pygame.init() #trying git

screen = pygame.display.set_mode((800, 600)) # w, h

done = False

color1 = (0, 128, 0xFF)
color2 = (255, 0, 0)
is_color1 = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_color1 = not is_color1
    
    if is_color1: color = color1
    else: color = color2
    
    pygame.draw.rect(screen, color, pygame.Rect(30, 50, 100, 60)) # x, y, w, h
    pygame.display.flip()