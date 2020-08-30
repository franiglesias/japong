import math


class ScoreManager(object):

    def __init__(self, player_one, player_two, match) -> None:
        if player_one.side == 'left':
            self.left = player_one
            self.right = player_two
        else:
            self.left = player_two
            self.right = player_one
        self.match = match

    def end_of_game(self):
        best = max(self.left.sets(), self.right.sets())
        target = math.ceil(self.match[0] / 2)
        return best >= target

    def end_of_set(self):
        difference = abs(self.left.points() - self.right.points())
        winner_points = max(self.left.points(), self.right.points())
        return difference >= 2 and winner_points >= self.match[1]

    def winner(self):
        if self.left.points() > self.right.points():
            return self.left

        return self.right

    def points(self):
        return self.left.points(), self.right.points()

    def partials(self):
        return self.left.partials(), self.right.partials()

    def sets(self):
        return self.left.sets(), self.right.sets()

    def end_set(self):
        if self.left.points() > self.right.points():
            self.left.win_set()
        else:
            self.right.win_set()

    def new_set(self):
        self.left.new_set()
        self.right.new_set()
