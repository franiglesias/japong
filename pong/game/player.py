from field.goal import Goal
from game.pad import Pad
from game.score import Score


class Player:
    def __init__(self, name, side, engine, speed=1):
        self.name = name
        self._score = Score()
        self.engine = engine
        self.side = side
        self.pad = Pad(side, speed, self.engine)
        self.goal = Goal(side.goal(), self)

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

    def beats(self, other):
        return self.points() > other.points()
