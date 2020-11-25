from pygame import Surface
from pygame.sprite import Sprite

from config import FPS
from config import white, red, lighten
from utils.soundplayer import SoundPlayer

GOAL_HIGHLIGHT_IN_SECONDS = 1.5


class Goal(Sprite):

    def __init__(self, x, player):
        super().__init__()

        self.image = Surface((10, 580))
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = x

        self.remaining = 0
        self.color = white
        self.player = player

    def hit(self):
        self.play_sound('point')
        self.color = red
        self.image.fill(self.color)

        self.remaining = FPS * GOAL_HIGHLIGHT_IN_SECONDS

    @staticmethod
    def play_sound(sound):
        player = SoundPlayer()
        player.play(sound)

    def update(self):
        self._update_color()
        self.image.fill(self.color)

    def _update_color(self):
        if self.remaining > 0:
            self.remaining -= 1
            self.color = lighten(self.color, 2)
