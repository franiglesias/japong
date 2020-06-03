import pygame

import pong.ponggame


class Window(object):
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title

    def run(self):
        size = (self.width, self.height)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption(self.title)

        pong.ponggame.ponggame(screen)
        return 0
