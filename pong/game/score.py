class Score(object):
    def __init__(self):
        self._sets = 0
        self._points = 0
        self._score = None

    def win_point(self):
        self._points += 1

    def points(self):
        return self._points

    def win_set(self):
        self._sets += 1

    def sets(self):
        return self._sets

    def new_set(self):
        if self._score is None:
            self._score = []
        self._score.append(self._points)
        self._points = 0

    def score(self):
        return self._score

    def end_match(self):
        self.new_set()
