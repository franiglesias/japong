from config import FPS


class Effect:
    def __init__(self, duration):
        self.duration = duration
        self.state = 0

    def start(self):
        self.state = FPS * self.duration

    def apply(self, target):
        if self.state <= 0:
            return
        self.state -= 1
        target.apply_effect()
