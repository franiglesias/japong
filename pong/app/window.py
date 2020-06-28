import pygame

import pong.game.game


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.title)

        self.score_board = None
        self.PLAY_AGAIN = 1

        self.game = pong.game.game.Game()

        self.scenes = []

    def run(self):
        exit_code = 0
        for scene in self.scenes:
            exit_code = scene.run()
            if self.is_error(exit_code):
                break
        if exit_code == self.PLAY_AGAIN:
            return self.run()
        return exit_code

    def add_scene(self, scene):
        self.scenes.append(scene)

    @staticmethod
    def is_error(exit_code):
        return exit_code < 0
