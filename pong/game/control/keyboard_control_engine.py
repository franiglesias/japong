from pygame import key, KEYDOWN, KEYUP

from config import HUMAN_SPEED
from game.control.control_engine import ControlEngine


class KeyboardControlEngine(ControlEngine):
    def __init__(self, keys):
        super().__init__()
        self.keys = keys

    def speed(self):
        return HUMAN_SPEED

    def handle(self, events):
        for event in events:
            self.__handle_keyboard_event(event)

    def __handle_keyboard_event(self, event):
        if event.type == KEYUP:
            self.__handle_released_keys(event)
        elif event.type == KEYDOWN:
            self.__handle_pressed_keys(event)

    def __handle_pressed_keys(self, event):
        if self._up_key_was_pressed(event):
            self.__move_pad_up()
        elif self._down_key_was_pressed(event):
            self._move_pad_down()

    def __handle_released_keys(self, event):
        if self.__control_key_was_released(event):
            self.__stop_pad()

    def __stop_pad(self):
        super().stop_pad()

    def __move_pad_up(self):
        super().move_pad_up()

    def _move_pad_down(self):
        super().move_pad_down()

    def _up_key_was_pressed(self, event):
        return self._get_key(event) == self.__up_key()

    def _down_key_was_pressed(self, event):
        return self._get_key(event) == self.__down_key()

    def _down_key_was_released(self, event):
        return self._get_key(event) == self.__down_key()

    def __up_key_was_released(self, event):
        return self._get_key(event) == self.__up_key()

    def __control_key_was_released(self, event):
        return self.__up_key_was_released(event) or self._down_key_was_released(event)

    def __up_key(self):
        return self.keys[0]

    def __down_key(self):
        return self.keys[1]

    @staticmethod
    def _get_key(event):
        return key.name(event.key)
