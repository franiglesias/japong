import pygame
from pygame.font import Font
from pygame.font import get_default_font

import pong.config
from pong.utils.textrenderer import TextRenderer


class TextWriter(object):
    def __init__(self, renderer: TextRenderer):
        self.writer = renderer
        self.surface = renderer.surface

    def blit(self, line, style):
        self.writer.blit(line, style)

    def multi_blit(self, lines, position):
        for line in lines:
            the_font = Font(get_default_font(), line[1]['font_size'])
            transparent = line[1]['background'] == 'transparent'

            if transparent:
                background = pong.config.chroma
            else:
                background = line[1]['background']

            text = the_font.render(line[0], False, line[1]['color'], background)
            if transparent:
                text.set_colorkey(background)

            if isinstance(position[0], str):
                if position[0] == 'center':
                    x = self.surface.get_rect().width // 2 - text.get_rect().width // 2
            else:
                x = position[0]

            self.surface.blit(text, (x, position[1]))

            position = (position[0], position[1] + text.get_rect().height)

