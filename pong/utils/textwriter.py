from pygame.font import Font
from pygame.font import get_default_font

from utils.line import Line, Position


class TextWriter(object):
    def __init__(self, surface):
        self.surface = surface

    def a_line(self, line, style):
        lines = [Line(line, style)]
        self.blits(lines, (style['horizontal'], style['vertical']))

    def blits(self, lines, position):
        for line in lines:
            the_font = Font(get_default_font(), line.font_size())
            text = the_font.render(line.content(), False, line.color(), line.background())

            p = Position.from_style(position[0], position[1], text, self.surface)

            if line.is_transparent():
                text.set_colorkey(line.background())

            self.surface.blit(text, p.coordinates())

            position = p.next(text).coordinates()
