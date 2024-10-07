import pygame
from pygame.locals import *
pygame.init()


clock = pygame.time.Clock()
fps = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')


class Nave(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  
        self.image = pygame.image.load('nave.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        V = 8

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= V   
        if key[pygame.K_RIGHT]:
            self.rect.x += V  


Nave_group = pygame.sprite.Group()

player = Nave(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100)
Nave_group.add(player)


bg = pygame.image.load('space.jpeg')
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_bg():
    screen.blit(bg, (0, 0))


run = True
while run:

    clock.tick(fps)

    
    draw_bg()

    player.update()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    
    Nave_group.draw(screen)

    
    pygame.display.update()


pygame.quit()
