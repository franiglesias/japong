from game.scoring.match import Match


class ScoreManager(object):

    def __init__(self, match) -> None:
        self.players = (None, None)
        self.match = match

    def register_players(self, one, two):
        if one.is_at_left():
            self.players = (one, two)
        else:
            self.players = (two, one)

    def left_player(self):
        return self.players[0]

    def right_player(self):
        return self.players[1]

    def end_of_game(self):
        return self._sets_won_by_best_player() >= self._sets_to_win_game()

    def end_of_set(self):
        return self._minimum_score_reached() and self._minimum_difference_reached()

    def _minimum_score_reached(self):
        return self._winner_points() >= self._points_to_win_set()

    def _minimum_difference_reached(self):
        return self._points_difference() >= 2

    def winner(self):
        if self.left_player().beats(self.right_player()):
            return self.left_player()

        return self.right_player()

    def _points_to_win_set(self):
        return self.match.points_to_win_set()

    def _sets_to_win_game(self):
        return self.match.sets_to_win_game()

    def _sets_won_by_best_player(self):
        return max(self.left_player().sets(), self.right_player().sets())

    def _winner_points(self):
        return max(self.left_player().points(), self.right_player().points())

    def _points_difference(self):
        return abs(self.left_player().points() - self.right_player().points())

    def points(self):
        return self.left_player().points(), self.right_player().points()

    def partials(self):
        return self.left_player().partials(), self.right_player().partials()

    def sets(self):
        return self.left_player().sets(), self.right_player().sets()

    def end_set(self):
        if self.left_player().beats(self.right_player()):
            self.left_player().win_set()
        else:
            self.right_player().win_set()

    def new_set(self):
        self.left_player().new_set()
        self.right_player().new_set()
