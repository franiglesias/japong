from pygame.sprite import Sprite, spritecollide, Group

from config import white, red, lighten
from field.bound_to_ball import BoundToBall
from field.effect import Effect
from field.positionable import Positionable
from game.ball import Ball
from utils.image import create_image
from utils.soundplayer import SoundPlayer

GOAL_HIGHLIGHT_IN_SECONDS = 1.5


class Goal(Sprite, Positionable, BoundToBall):

    def __init__(self, player):
        super().__init__()

        self.player = player
        self.color = white

        self.image = create_image(10, 580, self.color)
        self.rect = self.image.get_rect()
        self.set_position(self.player.side.goal_x(), 10)

        self.effect = Effect(GOAL_HIGHLIGHT_IN_SECONDS)

    def hit(self):
        self.play_sound()
        self.change_color()
        self.player.win_point()

    def change_color(self):
        self.color = red
        self.effect.start()

    def update(self):
        self.effect.apply(self)
        self.image.fill(self.color)

        self.__manage_ball_collision()

    def __manage_ball_collision(self):
        collisions = spritecollide(self, Group(self.ball), False)
        ball: Ball
        for ball in collisions:
            ball.goal()
            self.hit()

    def apply_effect(self):
        self.color = lighten(self.color, 2)

    @staticmethod
    def play_sound():
        SoundPlayer().play('point')
