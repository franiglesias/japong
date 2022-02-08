import pygame

from config import BASE_PATH


class SoundPlayer(object):
    def __init__(self) -> None:
        pygame.mixer.init()
        self.base = BASE_PATH + '/assets/sounds/'
        self.effects = {
            'pad-hit': 'pad-hit.ogg',
            'table-hit': 'table-hit.ogg',
            'point': 'point.ogg'
        }

    def play(self, effect):
        sound = pygame.mixer.Sound(self.base + self.effects[effect])
        sound.play()
