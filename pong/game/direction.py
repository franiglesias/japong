import random


class Direction:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def vertical_bounce(self):
        self.dy *= -1

    def horizontal_bounce(self, x_speed: int, y_speed: int):
        self.dx = x_speed * -(self.dx // abs(self.dx))
        self.dy = y_speed * (self.dy // abs(self.dy))

    def update(self, rect):
        rect.x += self.dx
        rect.y += self.dy

    @staticmethod
    def random():
        return random.choice([
            Direction(-1, -1),
            Direction(1, -1),
            Direction(1, 1),
            Direction(-1, 1)
        ])
