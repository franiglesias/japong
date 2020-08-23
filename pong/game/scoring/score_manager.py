from pong.config import POINTS_TO_WIN


class ScoreManager(object):

    def __init__(self, player_one, player_two) -> None:
        if player_one.side == 'left':
            self.left = player_one
            self.right = player_two
        else:
            self.left = player_two
            self.right = player_one

        self.target = POINTS_TO_WIN

    def end_of_game(self):
        return self.left.score() == self.target or self.right.score() == self.target

    def winner(self):
        if self.left.score() > self.right.score():
            return self.left

        return self.right

    def score(self):
        return self.left.score(), self.right.score()
