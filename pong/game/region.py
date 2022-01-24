class PadRegion():
    def __init__(self, height, pct):
        self.height = height
        self.pct = pct

    def hit(self, ball, pad):
        return ball.y_center() < self.height * self.pct // 100 + pad.rect.y

    def bounce(self, ball):
        ball.bounce_with_pad(1, 1)

    @staticmethod
    def where(ball, pad):
        for region in pad.regions:
            if region.hit(ball, pad):
                return region


class TopRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(1, -2)


class MiddleTopRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(2, 2)


class MiddleRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(1, 1)


class MiddleBottomRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(2, 2)


class BottomRegion(PadRegion):
    def bounce(self, ball):
        ball.bounce_with_pad(1, 2)
