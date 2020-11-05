import math


class Match(object):
    def __init__(self, match):
        self.sets = match[0]
        self.points_by_set = match[1]

    def points_to_win_set(self):
        return self.points_by_set

    def sets_to_win_game(self):
        return math.ceil(self.sets / 2)
