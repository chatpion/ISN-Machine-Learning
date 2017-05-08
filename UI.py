import pygame
from pygame.locals import *
from shoot_game import Game

pygame.init()
game = Game(1/4, 5, [0, 0])

fenetre = pygame.display.set_mode((64*(2*game.width + 1), 320))
perso = pygame.image.load("perso.png").convert_alpha()
bullet = pygame.image.load("bullet.png").convert_alpha()

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

    perso_coords = (0, 0)
    if game.is_jumping == 0:
        perso_coords = (320, 256)
    elif game.is_jumping == 1:
        perso_coords = (320, 192)
    else:
        perso_coords = (320, 128)
    fenetre.blit(perso, perso_coords)

    for i in game.bullets:
        fenetre.blit(bullet, (64*(5+i[0]), 256))
    for i in game.deadbullets:
        fenetre.blit(bullet, (64*(5+i[0]), 256))
    pygame.display.flip()
    