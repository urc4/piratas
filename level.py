import pygame
from settings import *
from player import Player
import math


class Level:
    def __init__(self):

        # get the display surface
        # self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.all_sprites = pygame.sprite.Group()
        self.player = Player([WIDTH/2, HEIGHT/2], [self.all_sprites])
        self.all_sprites.add(self.player)

    def run(self):
        # update and draw the game
        self.all_sprites.draw(pygame.display.get_surface())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if(self.player.angle + 5/(2*math.pi) > 2*math.pi):
                        self.player.angle = 0
                    else:
                        self.player.angle += 5/(2*math.pi)
                elif event.key == pygame.K_RIGHT:
                    if(self.player.angle - 5/(2*math.pi) < 0):
                        self.player.angle = 0
                    else:
                        self.player.angle -= 5/(2*math.pi)                
                elif event.key == pygame.K_UP:
                    self.player.velocity[1] -= 5*math.cos(self.player.angle)
                    if(self.player.angle <= math.pi):
                        self.player.velocity[0] -= 5*math.sin(self.player.angle) 
                    else:
                        self.player.velocity[0] += 5*math.cos(self.player.angle)        
                elif event.key == pygame.K_DOWN:
                    if(self.player.angle <= math.pi):
                        self.player.velocity[0] -= 5*math.sin(self.player.angle) 
                    else:
                        self.player.velocity[0] += 5*math.cos(self.player.angle)             
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pass 
                elif event.key == pygame.K_RIGHT:
                    pass 
                elif event.key == pygame.K_UP:
                    pass 
                elif event.key == pygame.K_DOWN:
                    pass 
        self.player.update()

