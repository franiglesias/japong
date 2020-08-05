from pygame.sprite import Sprite, spritecollide
from pygame.surface import Surface

from pong.config import white
from pong.game.control.control_engine import ControlEngine


class Pad(Sprite):
    def __init__(self, side, speed, engine: ControlEngine):
        super().__init__()

        self.speed = speed

        self.engine = engine
        self.engine.bind_pad(self)

        self.top_region_pct = 10
        self.middle_region_pct = 15

        self.width = 25
        self.height = 75

        self.dy = 0

        self.image = Surface((self.width, self.height))
        self.image.fill(white)

        self.rect = self.image.get_rect()

        if side == 'left':
            self.margin = 25
        else:
            self.margin = 775 - self.width

        self.rect.y = 300
        self.rect.x = self.margin
        self.borders = None

    def up(self):
        self.dy = -self.speed

    def down(self):
        self.dy = self.speed

    def stop(self):
        self.dy = 0

    def update(self):
        self.rect.y += self.dy

        for _ in spritecollide(self, self.borders, False):
            self.rect.y -= self.dy
            self.stop()

    def handle(self, *events):
        self.engine.handle(events)

    def hit(self, ball):
        ball_center_y = ball.rect.y + ball.radius - self.rect.y

        if ball_center_y < self.__top_region_limit():
            ball.bounce_with_pad_top()
        elif ball_center_y > self.__bottom_region_limit():
            ball.bounce_with_pad_bottom()
        elif self.__top_region_limit() <= ball_center_y < self.__upper_middle_limit():
            ball.bounce_middle_pad()
        elif self.__bottom_middle_limit() < ball_center_y <= self.__bottom_region_limit():
            ball.bounce_middle_pad()
        else:
            ball.bounce_with_pad()

    def __top_region_limit(self):
        return self.top_region_pct * self.height // 100

    def __upper_middle_limit(self):
        return (self.middle_region_pct + self.top_region_pct) * self.height // 100

    def __bottom_middle_limit(self):
        return ((100 - self.top_region_pct - self.middle_region_pct) * self.height) // 100

    def __bottom_region_limit(self):
        return ((100 - self.top_region_pct) * self.height) // 100
