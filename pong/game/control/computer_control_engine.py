from game.ball import Ball
from config import COMPUTER_MOVES_EVENT
from game.control.control_engine import ControlEngine


class ComputerControlEngine(ControlEngine):
    def __init__(self, ball: Ball):
        super().__init__()
        self.ball = ball

    def follow(self):
        if self._ball_position() > self._pad_position():
            self._move_pad_down()
        if self._ball_position() < self._pad_position():
            self._move_pad_up()

    def _ball_position(self):
        return self.ball.vertical_position()

    def handle(self, events):
        for event in events:
            if event.type == COMPUTER_MOVES_EVENT:
                self.follow()

    def _pad_position(self):
        return super().pad_position()

    def _move_pad_up(self):
        super().move_pad_up()

    def _move_pad_down(self):
        super().move_pad_down()
