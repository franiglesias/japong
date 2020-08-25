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
        difference = abs(self.left.score() - self.right.score())
        winner_points = max(self.left.score(), self.right.score())
        return difference >= 2 and winner_points >= self.match[1]

    def winner(self):
        if self.left.score() > self.right.score():
            return self.left

        return self.right

    def score(self):
        return self.left.score(), self.right.score()

    def end_set(self):
        if self.left.score() > self.right.score():
            self.left.win_set()
        else:
            self.right.win_set()

    def new_set(self):
        self.left.new_set()
        self.right.new_set()
