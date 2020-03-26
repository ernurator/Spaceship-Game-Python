import pygame
#pylint: disable=no-member

pygame.init()

screen = pygame.display.set_mode((800, 600)) # w, h

done = False

x, y = 30, 30
color1 = (0, 128, 0xFF)
color2 = (255, 0, 0)
is_color1 = True

while not done:
    for event in pygame.event.get():
        # Event on quit
        if event.type == pygame.QUIT:
            done = True
        # Changing color (space)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_color1 = not is_color1
    # Move
    
    # if event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_DOWN:
    #         y += 1
    #     if event.key == pygame.K_UP:
    #         y -= 1
    #     if event.key == pygame.K_LEFT:
    #         x -= 1
    #     if event.key == pygame.K_RIGHT:
    #         x += 1

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    
    if is_color1: color = color1
    else: color = color2

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) # x, y, w, h
    pygame.display.flip()