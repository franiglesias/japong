class Score(object):
    def __init__(self):
        self._sets = 0
        self._points = 0
        self._partials = None

    def win_point(self):
        self._points += 1

    def points(self):
        return self._points

    def win_set(self):
        self._sets += 1

    def sets(self):
        return self._sets

    def new_set(self):
        if self._partials is None:
            self._partials = []

        self._partials.append(self._points)
        self._points = 0

    def partials(self):
        return self._partials

    def end_match(self):
        self.new_set()
