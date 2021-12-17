from app.window import Window
from app.exit_code import ExitCode
from utils.textrenderer import TextRenderer
from utils.textwriter import TextWriter


class Scene(object):
    def __init__(self, window: Window):
        self.window = window
        self.text_renderer = TextWriter(TextRenderer(self.window.screen))

    def run(self):
        return ExitCode(0)
