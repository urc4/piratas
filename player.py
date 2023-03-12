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
        self.velocity = [0,0]
        self.position = pos
        self.angle = 0 # in radians
        self.rect.center = self.position
        
    def draw(self):
        pygame.draw.polygon(self.image,self.color,self.vertices)

    def update(self):
        self.position[0] += self.velocity[0]  
        self.position[1] += self.velocity[1]  
        self.rect.center = self.position
        self.draw()
