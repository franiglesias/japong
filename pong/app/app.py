import pygame

from pong.app.window import Window
from pong.scenes.endscene import EndScene
from pong.scenes.gamescene import GameScene
from pong.scenes.startscene import StartScene


class App(object):
    def __init__(self):
        self.window = Window(800, 600, 'Japong!')
        self.add_scene(StartScene(self.window))
        self.add_scene(GameScene(self.window))
        self.add_scene(EndScene(self.window))

    def run(self):
        pygame.init()
        code = self.window.run()

        pygame.quit()
        return code

    def add_scene(self, scene):
        self.window.add_scene(scene)
