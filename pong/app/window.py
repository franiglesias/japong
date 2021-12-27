import pygame

from app.exit_code import ExitCode
from game.game import Game


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.screen = self.set_up_screen(width, height, title)
        self.game = Game()
        self.score_board = None
        self.scenes = []

    @staticmethod
    def set_up_screen(width: int, height: int, title: str):
        pygame.display.set_caption(title)
        return pygame.display.set_mode((width, height))

    def run(self):
        return self.run_or_exit(self.run_scenes())

    def run_or_exit(self, status):
        if status.is_play_again():
            return self.run()
        return status

    def run_scenes(self):
        for scene in self.scenes:
            code = scene.run()
            if code.is_error():
                return code
        return ExitCode(0)

    def add_scene(self, scene):
        self.scenes.append(scene)

