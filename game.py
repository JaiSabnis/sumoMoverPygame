import pygame
from player import Player

black = (0,0,0)
white = (255,250,255)



pygame.init()

width = 1280
height = 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

icon = pygame.image.load("images/battleship.png")
pygame.display.set_icon(icon)

forestBackground = pygame.image.load("images/forest.png")
skyBackground = pygame.image.load("images/sky.png")
background = skyBackground



def redrawWindow(window,player):
    window.fill(black)
    window.blit(background, (0,0))
    player.draw()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    player1 = Player(window, 100, 150, white)


    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        player1.move()
        redrawWindow(window, player1)

main()