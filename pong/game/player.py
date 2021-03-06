from field.goal import Goal
from game.pad import Pad
from game.score import Score


class Player:
    def __init__(self, name, side, engine, speed=1):
        self.name = name
        self._score = Score()
        self.engine = engine
        self.side = side
        self.pad = Pad(self.side, speed, self.engine)
        if self.is_at_left():
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

    def is_at_left(self):
        return self.side == 'left'

    def beats(self, other):
        return self.points() > other.points()
