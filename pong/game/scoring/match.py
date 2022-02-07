import math


class Match(object):
    def __init__(self, sets: int, points_by_set: int, minimum_diff: int = 2):
        self.sets = sets
        self.points_by_set = points_by_set
        self.minimum_diff = minimum_diff

    def minimum_difference_reached(self, difference):
        return difference >= self.minimum_diff

    def minimum_score_reached(self, points):
        return points >= self.points_by_set

    def minimum_sets_reached(self, sets):
        return sets >= math.ceil(self.sets / 2)
