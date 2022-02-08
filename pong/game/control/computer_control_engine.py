from config import COMPUTER_MOVES_EVENT, COMPUTER_SPEED
from game.ball import Ball
from game.control.control_engine import ControlEngine


class ComputerControlEngine(ControlEngine):
    def __init__(self, ball: Ball):
        super().__init__()
        self.ball = ball

    def handle(self, events):
        for event in events:
            if event.type == COMPUTER_MOVES_EVENT:
                self.__follow()

    def speed(self):
        return COMPUTER_SPEED

    def __follow(self):
        if self.__should_move_down():
            self.__move_pad_down()
        if self.__should_move_up():
            self.__move_pad_up()

    def __should_move_up(self):
        return self.__ball_position() < self.__pad_position()

    def __should_move_down(self):
        return self.__ball_position() > self.__pad_position()

    def __ball_position(self):
        return self.ball.vertical_position()

    def __pad_position(self):
        return super().pad_position()

    def __move_pad_up(self):
        super().move_pad_up()

    def __move_pad_down(self):
        super().move_pad_down()
