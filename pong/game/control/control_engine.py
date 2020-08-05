from abc import ABCMeta, abstractmethod


class ControlEngine(object, metaclass=ABCMeta):
    def __init__(self):
        self.pad = None

    def bind_pad(self, the_pad):
        self.pad = the_pad

    @abstractmethod
    def handle(self, events):
        pass
