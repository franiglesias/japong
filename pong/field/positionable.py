class Positionable:
    rect = None

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def vertical_position(self):
        return self.rect.y
