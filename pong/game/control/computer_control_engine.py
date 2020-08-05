from pong.ball import Ball
from pong.config import COMPUTER_MOVES_EVENT
from pong.game.control.control_engine import ControlEngine


class ComputerControlEngine(ControlEngine):
    def __init__(self, the_ball: Ball):
        super().__init__()
        self.ball = the_ball

    def follow(self):
        if self.ball.rect.y > self.pad.rect.y:
            self.pad.down()
        if self.ball.rect.y < self.pad.rect.y:
            self.pad.up()

    def handle(self, events):
        for event in events:
            if event.type == COMPUTER_MOVES_EVENT:
                self.follow()
