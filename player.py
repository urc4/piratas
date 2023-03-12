import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,100),pygame.SRCALPHA)
        self.vertices = [(0,50),(25,100),(50,50),(25,0)]
        self.color = (255,0,0)
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def draw(self):
        pygame.draw.polygon(self.image,self.color,self.vertices)

    def update(self):
        pass
