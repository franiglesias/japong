from pygame.font import Font
from pygame.font import get_default_font

import pong.config
from pong.utils.textrenderer import TextRenderer


class TextWriter(object):
    def __init__(self, renderer: TextRenderer):
        self.writer = renderer
        self.surface = renderer.surface
        self.HORIZONTAL = 0
        self.VERTICAL = 1
        self.STYLE = 1
        self.TEXT = 0

    def blit(self, line, style):
        self.writer.blit(line, style)

    def multi_blit(self, lines, position):
        for line in lines:
            the_font = Font(get_default_font(), line[self.STYLE]['font_size'])
            transparent = line[self.STYLE]['background'] == 'transparent'
            background = self._background(line, transparent)

            text = the_font.render(line[self.TEXT], False, line[self.STYLE]['color'], background)
            if transparent:
                text.set_colorkey(background)

            self.surface.blit(text, ((self._x(position, text)), position[self.VERTICAL]))
            position = self.position_next_line(position, text)

    def _x(self, position, text):
        if self._center(position):
            return (self.surface.get_rect().width - text.get_rect().width) // 2
        return position[0]

    def position_next_line(self, position, text):
        return position[self.HORIZONTAL], position[self.VERTICAL] + text.get_rect().height

    def _background(self, line, transparent):
        if transparent:
            return pong.config.chroma

        return line[self.STYLE]['background']

    def _center(self, position):
        return isinstance(position[self.HORIZONTAL], str) and position[self.HORIZONTAL] == 'center'
