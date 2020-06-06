import pygame

import pong.config


class TextRenderer():
    def __init__(self, surface):
        self.surface = surface

    def blit(self, font_size, text_to_render, horizontal, vertical):
        the_font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        text = the_font.render(text_to_render, True, pong.config.white, pong.config.black)
        text.set_colorkey(pong.config.black)
        x = 0
        y = 0
        if horizontal == 'center':
            x = self.surface.get_rect().width // 2 - text.get_rect().width // 2

        if vertical == 'bottom':
            y = self.surface.get_rect().height - 30 - text.get_rect().height
        if vertical == 'middle':
            y = self.surface.get_rect().height // 2 - text.get_rect().height // 2

        self.surface.blit(text, (x, y))
