class Direction:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def border_bounce(self):
        self.dy *= -1

    def pad_bounce(self, x_speed: int, y_speed: int):
        self.dx = x_speed * -(self.dx // abs(self.dx))
        self.dy = y_speed * (self.dy // abs(self.dy))

    def update(self, rect):
        rect.x += self.dx
        rect.y += self.dy

    def horiz_rebound(self, rect):
        rect.x -= self.dx

    def vertical_rebound(self, rect):
        rect.y -= self.dy