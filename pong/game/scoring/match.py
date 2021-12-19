import math


class Match(object):
    def __init__(self, sets: int, points_by_set: int):
        self.sets = sets
        self.points_by_set = points_by_set

    def points_to_win_set(self):
        return self.points_by_set

    def sets_to_win_game(self):
        return math.ceil(self.sets / 2)
