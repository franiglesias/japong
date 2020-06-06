import pygame

import pong.app.window
import pong.config
import pong.scenes.gamescene
import pong.scenes.endscene

pygame.init()
pygame.mixer.init()

playerHit = pygame.mixer.Sound(pong.config.basepath + '/sounds/player.wav')
sideHit = pygame.mixer.Sound(pong.config.basepath + '/sounds/side.wav')
point = pygame.mixer.Sound(pong.config.basepath + '/sounds/ohno.wav')


class App(object):
    def __init__(self):
        self.window = pong.app.window.Window(800, 600, 'Japong!')
        self.window.add_scene(pong.scenes.gamescene.GameScene(self.window))
        self.window.add_scene(pong.scenes.endscene.EndScene(self.window))

    def run(self):
        return self.window.run()
