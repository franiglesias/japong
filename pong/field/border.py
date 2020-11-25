import pygame

from config import white
from utils.soundplayer import SoundPlayer


class Border(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()

        self.image = pygame.Surface((800, 10))
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0

    @staticmethod
    def hit():
        player = SoundPlayer()
        player.play('table-hit')
