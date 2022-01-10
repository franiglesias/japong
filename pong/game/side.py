class Side:
    def pad(self):
        return 0

    def goal(self):
        return 0

    @staticmethod
    def from_raw(side):
        if side == 'left':
            return Left()
        else:
            return Right()

    def opposite(self):
        pass

    def is_left(self):
        pass

    def str(self):
        return '?'


class Left(Side):
    def pad(self):
        return 25

    def goal(self):
        return 0

    def opposite(self):
        return Right()

    def is_left(self):
        return True

    def str(self):
        return 'left'


class Right(Side):
    def pad(self):
        return 750

    def goal(self):
        return 790

    def opposite(self):
        return Left()

    def is_left(self):
        return False

    def str(self):
        return 'right'
