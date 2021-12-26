from pygame import Surface
from pygame.sprite import Sprite, spritecollide

from config import white, red, lighten
from field.effect import Effect
from game.ball import Ball
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

        self.balls = None

    def bind_ball(self, ball: Ball):
        self.balls = [ball]

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

        self.__manage_ball_collision()

    def __manage_ball_collision(self):
        collisions = spritecollide(self, self.balls, False)
        ball: Ball
        for ball in collisions:
            ball.goal()
            self.hit()

    def apply_effect(self):
        self.color = lighten(self.color, 2)
