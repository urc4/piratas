import pygame
from settings import *
from player import Player


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.all_sprites = pygame.sprite.Group()
        self.player = Player((WIDTH/2, HEIGHT/2), [self.all_sprites])
        self.all_sprites.add(self.player)

    def run(self):
        # update and draw the game
        self.all_sprites.draw(self.display_surface)
