class ScoreManager(object):

    def __init__(self, match) -> None:
        self.players = (None, None)
        self.match = match

    def register_players(self, one, two):
        if one.side.is_left():
            self.players = (two, one)
        else:
            self.players = (one, two)

    def left_player(self):
        return self.players[0]

    def right_player(self):
        return self.players[1]

    def end_of_game(self):
        return self.__sets_won_by_best_player() >= self.__sets_to_win_game()

    def end_of_set(self):
        return self.__minimum_score_reached() and self.__minimum_difference_reached()

    def winner(self):
        if self.left_player().beats(self.right_player()):
            return self.left_player()

        return self.right_player()

    def __minimum_difference_reached(self):
        return self.__points_difference() >= 2

    def __minimum_score_reached(self):
        return self.__winner_points() >= self.__points_to_win_set()

    def __points_to_win_set(self):
        return self.match.points_to_win_set()

    def __sets_to_win_game(self):
        return self.match.sets_to_win_game()

    def __sets_won_by_best_player(self):
        return max(self.left_player().sets(), self.right_player().sets())

    def __winner_points(self):
        return max(self.left_player().points(), self.right_player().points())

    def __points_difference(self):
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
