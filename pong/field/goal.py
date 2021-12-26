from pygame import Surface
from pygame.sprite import Sprite

from config import white, red, lighten
from field.effect import Effect
from utils.soundplayer import SoundPlayer

GOAL_HIGHLIGHT_IN_SECONDS = 1.5


class Goal(Sprite):

    def __init__(self, x, player):
        super().__init__()

        self.color = white

        self.width = 10
        self.height = 580

        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = x

        self.effect = Effect(GOAL_HIGHLIGHT_IN_SECONDS)
        self.player = player

    def hit(self):
        self.play_sound()
        self.change_color()
        self.player.win_point()

    def change_color(self):
        self.color = red
        self.effect.start()

    @staticmethod
    def play_sound():
        SoundPlayer().play('point')

    def update(self):
        self.effect.apply(self)
        self.image.fill(self.color)

    def apply_effect(self):
        self.color = lighten(self.color, 2)
