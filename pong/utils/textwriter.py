from pygame.font import Font
from pygame.font import get_default_font

from utils.line import Line, Position


class TextWriter(object):
    def __init__(self, surface):
        self.surface = surface

    def a_line(self, line, style):
        lines = [(line, style)]
        self.multi_blit(lines, (style['horizontal'], style['vertical']))

    def multi_blit(self, lines, position):
        for line in lines:
            ln = Line(line[0], line[1])

            the_font = Font(get_default_font(), ln.font_size())
            text = the_font.render(ln.content(), False, ln.color(), ln.background())

            p = Position.from_style(position[0], position[1], text, self.surface)

            if ln.is_transparent():
                text.set_colorkey(ln.background())

            self.surface.blit(text, p.coordinates())

            position = p.next(text).coordinates()
