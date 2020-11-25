import pygame

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

    def game_side(self):
        return self.game.side_preference

    def game_mode(self):
        return self.game.game_mode

    def set_side(self, side):
        self.game.set_side_preference(side)

    def set_mode(self, mode):
        self.game.set_game_mode(mode)
