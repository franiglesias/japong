import pygame

import pong.config


class TextRenderer():
    def __init__(self, surface):
        self.surface = surface
        self.padding = 30

    def blit(self, text_to_render, style):
        the_font = pygame.font.Font(pygame.font.get_default_font(), style['font_size'])
        transparent = style['background'] == 'transparent'

        if transparent:
            background = pong.config.chroma
        else:
            background = style['background']

        text = the_font.render(text_to_render, False, style['color'], background)
        if transparent:
            text.set_colorkey(background)

        position = self.compute_position(text, style['horizontal'], style['vertical'])
        self.surface.blit(text, position)

    def compute_position(self, text, horizontal, vertical):
        x = 0
        y = 0
        if horizontal == 'left':
            x = self.padding
        if horizontal == 'center':
            x = self.surface.get_rect().width // 2 - text.get_rect().width // 2
        if horizontal == 'right':
            x = self.surface.get_rect().width - text.get_rect().width - self.padding
        if vertical == 'top':
            y = self.padding
        if vertical == 'middle':
            y = self.surface.get_rect().height // 2 - text.get_rect().height // 2
        if vertical == 'bottom':
            y = self.surface.get_rect().height - text.get_rect().height - self.padding
        return x, y
