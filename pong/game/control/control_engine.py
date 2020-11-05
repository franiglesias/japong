from abc import ABCMeta, abstractmethod


class ControlEngine(object, metaclass=ABCMeta):
    def __init__(self):
        self.pad = None

    def bind_pad(self, the_pad):
        self.pad = the_pad

    @abstractmethod
    def handle(self, events):
        pass

    def _pad(self):
        return self.pad

    def pad_position(self):
        return self._pad().vertical_position()

    def move_pad_up(self):
        self._pad().up()

    def move_pad_down(self):
        self._pad().down()

    def stop_pad(self):
        self._pad().stop()
