import pygame

playerRadius = 30
playerThiccness = round(playerRadius/10)
bulletWidth = 25
bulletHieght = 5

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
NONE = "none"

gameWidth = 1280
gameHeight = 720

class Bullet():
    def __init__(self, window, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vel = 8
        self.rect = (x, y, bulletWidth, bulletHieght)
        self.window = window
        self.fired = False
        self.direction = NONE


    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def shoot(self, direction):
        self.fired = True
        self.direction = direction

        while self.fired:
            self.update()

    def update(self):
        if self.x <= playerRadius or self.x >= gameWidth - playerRadius:
            self.fired = False

        if self.fired:
            if self.direction == RIGHT or self.direction == NONE:
                self.rect = (self.x + self.vel, self.y, bulletWidth, bulletHieght)
            if self.direction == LEFT:
                self.rect = (self.x - self.vel, self.y, bulletWidth, bulletHieght)
            self.draw()
