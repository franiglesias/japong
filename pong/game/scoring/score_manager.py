import math


class ScoreManager(object):

    def __init__(self, player_one, player_two, match) -> None:
        if player_one.is_at_left():
            self.left = player_one
            self.right = player_two
        else:
            self.left = player_two
            self.right = player_one
        self.match = match

    def end_of_game(self):
        return self._best() >= self._target()

    def end_of_set(self):
        return self._difference() >= 2 and self._winner_points() >= self.match[1]

    def winner(self):
        if self.left.beats(self.right):
            return self.left

        return self.right

    def _target(self):
        return math.ceil(self.match[0] / 2)

    def _best(self):
        return max(self.left.sets(), self.right.sets())

    def _winner_points(self):
        return max(self.left.points(), self.right.points())

    def _difference(self):
        return abs(self.left.points() - self.right.points())

    def points(self):
        return self.left.points(), self.right.points()

    def partials(self):
        return self.left.partials(), self.right.partials()

    def sets(self):
        return self.left.sets(), self.right.sets()

    def end_set(self):
        if self.left.beats(self.right):
            self.left.win_set()
            return

        self.right.win_set()

    def new_set(self):
        self.left.new_set()
        self.right.new_set()
