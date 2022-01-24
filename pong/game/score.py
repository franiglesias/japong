class Score(object):
    def __init__(self):
        self.__sets = 0
        self.__points = 0
        self.__partials = None

    def win_point(self):
        self.__points += 1

    def points(self):
        return self.__points

    def win_set(self):
        self.__sets += 1

    def sets(self):
        return self.__sets

    def new_set(self):
        if self.__partials is None:
            self.__partials = []

        self.__partials.append(self.__points)
        self.__points = 0

    def partials(self):
        return self.__partials

    def end_match(self):
        self.new_set()
