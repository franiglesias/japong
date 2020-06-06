from pong.app.window import Window
from pong.utils.textrenderer import TextRenderer


class Scene(object):
    def __init__(self, window: Window):
        self.window = window
        self.text_renderer = TextRenderer(self.window.screen)

    def run(self):
        return 0
