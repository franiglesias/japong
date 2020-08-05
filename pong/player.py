from pong.game.pad import Pad
from pong.goal import Goal


class Player:
    def __init__(self, name, side, engine, speed=1):
        self.name = name
        self.score = 0
        self.engine = engine
        self.side = side
        self.pad = Pad(self.side, speed, self.engine)
        if side == 'left':
            self.goal = Goal(790, self)
        else:
            self.goal = Goal(0, self)

    def win_point(self):
        self.score += 1

    def handle(self, event):
        self.pad.handle(event)
