import pygame
import random
from enum import Enum
#pylint: disable=no-member

pygame.init()

screen = pygame.display.set_mode((800, 600)) # w, h
pygame.display.set_caption('Space blaster')
backgroundImage = pygame.image.load('res/background.jpg')


class Direction(Enum):
    LEFT = 3
    RIGHT = 4


##########################################    Player    ##########################################


class Player:
    def __init__(self):
        self.image = pygame.image.load('res/spaceship.png')
        self.x = 300
        self.y = screen.get_size()[1] - self.image.get_size()[1] - 16
        self.dx = 400
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def move(self, direction, sec):
        if direction == Direction.RIGHT and self.x < screen.get_size()[0] - self.image.get_size()[0]:    
            self.x += int(sec * self.dx)
        if direction == Direction.LEFT and self.x > 0:
            self.x -= int(sec * self.dx)


##########################################    Enemy    ##########################################


class Enemy():
    def __init__(self):
        self.image = pygame.image.load('res/ufo.png')
        self.x = random.randint(1, screen.get_size()[0] - self.image.get_size()[0] - 1)
        self.y = random.randint(20, 50)
        self.direction = random.choice((Direction.LEFT, Direction.RIGHT))
        self.dx = 800 // 3
        self.dy = 50

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def move(self, sec):
        self.x += int(self.dx*sec) if self.direction == Direction.RIGHT else -int(self.dx*sec)

        if self.x > screen.get_size()[0] - self.image.get_size()[0] or self.x < 0:
            self.direction = Direction.LEFT if self.direction == Direction.RIGHT else Direction.RIGHT
            self.y += self.dy


##########################################    Bullet    ##########################################


class Bullet():
    def __init__(self, x, y):
        self.image = pygame.image.load('res/bullet.png')
        self.x = x - self.image.get_size()[0] // 2
        self.y = y - self.image.get_size()[1] - 4
        self.dy = -600

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, sec):
        self.y += int(self.dy * sec)
        if self.y < 0:
            global fired
            fired = False
            del self


##########################################    Collisions    #########################################


def checkCollisions(bullet, enemies):
    global score
    global fired
    for i in range(len(enemies)):
        dist_x = bullet.x - enemies[i].x
        dist_y = bullet.y - enemies[i].y
        if -24 <= dist_x <= 64 and -24 <= dist_y <= 64 and fired:
            fired = False
            del bullet
            del enemies[i]
            score += 1
            break

def drawScore():
    global score
    font = pygame.font.SysFont('Courier', 24, bold=True)
    text = font.render(f'Score: {score}', True, (238, 238, 238))
    screen.blit(text, (800 - text.get_width() - 20, 20))


##########################################    Init    ##########################################


player = Player()
enemies = [Enemy()]

done = False
fired = False
score = 0

FPS = 60
clock = pygame.time.Clock()
interval = 1.5
cycletime = 0

##########################################    Main loop    ##########################################


while not done:
    millis = clock.tick(FPS)
    sec = millis / 1000
    cycletime += sec

    if cycletime > interval:
        cycletime = 0
        enemies.append(Enemy())

    for event in pygame.event.get():
        # Event on quit
        if event.type == pygame.QUIT:
            done = True
       
    ##########################    Spaceship movement    ##########################
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        player.move(Direction.LEFT, sec)
    if pressed[pygame.K_RIGHT]:
        player.move(Direction.RIGHT, sec)

    ###########################    Firing    ##########################
    if pressed[pygame.K_SPACE] and not fired:
        fired = True
        global bullet
        bullet = Bullet(player.x + player.image.get_size()[0] // 2, player.y)
    
    ##########################    Drawings and other movements    ##########################
    screen.blit(backgroundImage, (0, 0))
    player.draw()
    for enemy in enemies:
        enemy.move(sec)
        enemy.draw()

    if fired:
        bullet.move(sec)
        bullet.draw()
        checkCollisions(bullet, enemies)

    drawScore()
    pygame.display.flip()