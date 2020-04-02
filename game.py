import pygame
import random
#pylint: disable=no-member

pygame.init()

screen = pygame.display.set_mode((800, 600)) # w, h
pygame.display.set_caption('Space blaster')


##########################################    Objects init    ##########################################


playerImage = pygame.image.load('res/spaceship.png')
enemyImage = pygame.image.load('res/ufo.png')
backgroundImage = pygame.image.load('res/background.jpg')
bulletImage = pygame.image.load('res/bullet.png')

player_x, player_y = 300, 520
enemy_x, enemy_y = random.randint(0, 736), random.randint(20, 50)
bullet_x, bullet_y = 0, 600
enemy_dx = 10
enemy_dy = 50
bullet_dy = -30


##########################################    Drawings    ##########################################


def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def background():
    screen.blit(backgroundImage, (0, 0))

def bullet(x, y):
    screen.blit(bulletImage, (x, y))

def drawScore():
    global score
    font = pygame.font.SysFont('Courier', 24, bold=True)
    text = font.render(f'Score: {score}', True, (238, 238, 238))
    screen.blit(text, (800 - text.get_width() - 20, 20))



##########################################    Init    ##########################################


done = False
fired = False
score = 0

clock = pygame.time.Clock()


##########################################    Main loop    ##########################################


while not done:
    clock.tick(30)
    for event in pygame.event.get():
        # Event on quit
        if event.type == pygame.QUIT:
            done = True
       
    ##########################    Spaceship movement    ##########################
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        player_x -= 14
    if pressed[pygame.K_RIGHT]:
        player_x += 14

    ###########################    Firing    ##########################
    if pressed[pygame.K_SPACE] and not fired:
        fired = True
        bullet_x = player_x + 20
        bullet_y = player_y - 25
    
    ##########################    Enemy movement    ##########################
    enemy_x += enemy_dx

    if enemy_x > 736 or enemy_x < 0:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy

    ##########################    Bullet movement    ##########################
    if fired: bullet_y += bullet_dy

    if bullet_y < 0:
        fired = False
        bullet_x, bullet_y = 0, 600

    ##########################    Collisions    ##########################
    dist_x = bullet_x - enemy_x
    dist_y = bullet_y - enemy_y
    if -24 <= dist_x <= 64 and -24 <= dist_y <= 64 and fired:
        fired = False
        score += 1
        bullet_x, bullet_y = 0, 600
        enemy_x, enemy_y = random.randint(0, 736), random.randint(20, 50)

        
    ##########################    Drawings    ##########################
    background()
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    if fired: bullet(bullet_x, bullet_y)
    drawScore()
    pygame.display.flip()