from game.score import Score


class Player:
    def __init__(self, name, side):
        self.name = name
        self.score = Score()
        self.side = side

    def win_point(self):
        self.score.win_point()

    def points(self):
        return self.score.points()

    def partials(self):
        return self.score.partials()

    def new_set(self):
        self.score.new_set()

    def win_set(self):
        self.score.win_set()

    def sets(self):
        return self.score.sets()

    def beats(self, other):
        return self.points() > other.points()
