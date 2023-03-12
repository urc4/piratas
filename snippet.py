import pygame
import sys
# Display screen settings
WIDTH = 1280
HEIGHT = 720
FPS = 30



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Piratas')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('blue')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.all_sprites = pygame.sprite.Group()
        self.player = Player((100, 100), [self.all_sprites])
        self.all_sprites.add(self.player)

    def run(self):
        # update and draw the game
        self.all_sprites.draw(self.display_surface)



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.vertices = [(100,100),(125,150),(150,100),(125,50)]
        self.color = (255,0,0)
        self.draw()
        # self.image = pygame.Surface((50, 50))
        # self.image.fill('brown')
        # self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH/2, HEIGHT/2)
    def draw(self):
        pygame.draw.polygon(window,self.color,self.vertices)

    def update(self):
        pass
