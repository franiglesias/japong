import pygame

from app.exit_code import ExitCode
from game.game import Game


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.size = (width, height)
        self.title = title
        self.screen = pygame.display.set_mode(self.size)

        pygame.display.set_caption(self.title)

        self.score_board = None
        self.PLAY_AGAIN = 1

        self.game = Game()
        self.scenes = []

    def run(self):
        status = self.run_scenes()
        if status.is_play_again():
            return self.run()
        return status.value()

    def run_scenes(self):
        for scene in self.scenes:
            code = scene.run()
            if code.is_error():
                return code
        return ExitCode(0)

    def add_scene(self, scene):
        self.scenes.append(scene)

    def game_side(self):
        return self.game.side_preference

    def game_mode(self):
        return self.game.game_mode

    def set_side(self, side):
        self.game.set_side_preference(side)

    def set_mode(self, mode):
        self.game.set_game_mode(mode)
