class Side:
    def pad_x(self):
        return 0

    def goal_x(self):
        return 0

    def is_left(self):
        pass

    def str(self):
        return '?'

    def equals(self, other):
        return type(self) == type(other)

    @staticmethod
    def from_raw(side):
        if side == 'left':
            return Left()
        else:
            return Right()


class Left(Side):
    def pad_x(self):
        return 25

    def goal_x(self):
        return 0

    def is_left(self):
        return True

    def str(self):
        return 'left'


class Right(Side):
    def pad_x(self):
        return 750

    def goal_x(self):
        return 790

    def is_left(self):
        return False

    def str(self):
        return 'right'
