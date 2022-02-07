from abc import ABCMeta, abstractmethod


class ControlEngine(metaclass=ABCMeta):
    def __init__(self):
        self.pad = None

    def bind_pad(self, the_pad):
        self.pad = the_pad

    def speed(self):
        return 1

    @abstractmethod
    def handle(self, events):
        pass

    def pad_position(self):
        return self.pad.vertical_position()

    def move_pad_up(self):
        self.pad.up()

    def move_pad_down(self):
        self.pad.down()

    def stop_pad(self):
        self.pad.stop()
