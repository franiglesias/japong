class ExitCode:
    def __init__(self, code: int):
        self.__code = code

    def is_error(self):
        return self.__code < 0

    def is_play_again(self):
        return self.__code == 1

    def value(self):
        return self.__code

    def equals(self, other):
        return self.value() == other.value()

    @staticmethod
    def play_again():
        return ExitCode(1)

    @staticmethod
    def success():
        return ExitCode(0)
