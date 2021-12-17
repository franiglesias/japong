class ExitCode(object):
    def __init__(self, code: int):
        self.code = code

    def is_error(self):
        return self.code < 0

    def is_play_again(self):
        return self.code == 1

    def value(self):
        return self.code

    @staticmethod
    def play_again():
        return ExitCode(1)

    @staticmethod
    def success():
        return ExitCode(0)
