from pong.game.score import Score
from pong.game.pad import Pad
from pong.goal import Goal


class Player:
    def __init__(self, name, side, engine, speed=1):
        self.name = name
        self._score = Score()
        self.engine = engine
        self.side = side
        self.pad = Pad(self.side, speed, self.engine)
        if side == 'left':
            self.goal = Goal(790, self)
        else:
            self.goal = Goal(0, self)

    def win_point(self):
        self._score.win_point()

    def handle(self, event):
        self.pad.handle(event)

    def points(self):
        return self._score.points()

    def partials(self):
        return self._score.partials()

    def new_set(self):
        self._score.new_set()

    def win_set(self):
        self._score.win_set()

    def sets(self):
        return self._score.sets()

