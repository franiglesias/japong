import pygame

import pong.config


class Border(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()

        self.image = pygame.Surface((800, 10))
        self.image.fill(pong.config.white)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0
