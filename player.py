import pygame
from bullet import Bullet

playerRadius = 30
playerThiccness = round(playerRadius/10)

headRadius = round(playerRadius/2.2)
headDistance = playerRadius + (playerThiccness *6)

handRadius = 10


LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
NONE = "none"

GRAVITY = 10

headPosition = {
        NONE: 0,
        LEFT: -30,
        RIGHT: 30,
    }

gameWidth = 1280
gameHeight = 720


class Player():
    def __init__(self, window, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.location = (x,y)
        self.headMoving = True
        self.headLocation = 0
        self.vel = 8
        self.window = window
        self.direction = NONE

    def draw(self):
        self.drawHead()
        pygame.draw.circle(self.window, self.color, self.location, playerRadius, playerThiccness)

    def drawHead(self):
        headOffset = headPosition.get(self.direction, 0)
        headLocation = (self.x + headOffset, self.y - headDistance)
        pygame.draw.circle(self.window, self.color, headLocation, headRadius, playerThiccness)

    def move(self):
        keys = pygame.key.get_pressed()
        '''
        noKeysPressed = not (keys[pygame.K_LEFT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_SPACE])
        if noKeysPressed:
            self.direction = NONE
            '''

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.direction = LEFT

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.direction = RIGHT

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.direction = NONE

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.y += GRAVITY
        self.update()

    def update(self):
        if self.x <= playerRadius:
            self.x = playerRadius
        elif self.x >= gameWidth - playerRadius:
            self.x = gameWidth - playerRadius

        self.location = (self.x, self.y)
