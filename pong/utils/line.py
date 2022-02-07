from config import chroma


class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__padding = 30

    @staticmethod
    def from_style(horizontal, vertical, text, surface):
        coordinates = position(horizontal, vertical, text, surface, 30)
        return Position(coordinates[0], coordinates[1])

    def coordinates(self):
        return self.__x, self.__y

    def next(self, text):
        return Position(self.__x, self.__y + text.get_rect().height)


def position(horizontal, vertical, text, surface, padding):
    x = 0
    y = 0
    if horizontal == 'left':
        x = padding
    if horizontal == 'center':
        x = surface.get_rect().width // 2 - text.get_rect().width // 2
    if horizontal == 'right':
        x = surface.get_rect().width - text.get_rect().width - padding
    if vertical == 'top':
        y = padding
    if vertical == 'middle':
        y = surface.get_rect().height // 2 - text.get_rect().height // 2
    if vertical == 'bottom':
        y = surface.get_rect().height - text.get_rect().height - padding
    if isinstance(horizontal, int):
        x = horizontal
    if isinstance(vertical, int):
        y = vertical
    return x, y


class Line:
    def __init__(self, content, style):
        self.__content = content
        self.__style = style

    def content(self):
        return self.__content

    def font_size(self):
        return self.__style['font_size']

    def color(self):
        return self.__style['color']

    def background(self):
        if self.is_transparent():
            return chroma

        return self.__style['background']

    def is_transparent(self):
        return self.__style['background'] == 'transparent'
