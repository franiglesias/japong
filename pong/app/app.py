import pygame

import pong.app.window
import pong.config
import pong.ponggame

pygame.init()
pygame.mixer.init()

playerHit = pygame.mixer.Sound(pong.config.basepath + '/sounds/player.wav')
sideHit = pygame.mixer.Sound(pong.config.basepath + '/sounds/side.wav')
point = pygame.mixer.Sound(pong.config.basepath + '/sounds/ohno.wav')


class App():
    def __init__(self):
        self.window = pong.app.window.Window(800, 600, 'Japong!')

    def run(self):
        return self.window.run()

