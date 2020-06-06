import pygame

import pong.ponggame


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.title)

        self.score_board = None

    def run(self):
        pong.ponggame.ponggame(self.screen)
        return 0
