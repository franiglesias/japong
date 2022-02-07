from app.exit_code import ExitCode
from app.window import Window
from utils.textwriter import TextWriter


class Scene(object):
    def __init__(self, window: Window):
        self.window = window
        self.text_writer = TextWriter(self.window.screen)

    def run(self):
        return ExitCode(0)
