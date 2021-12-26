from pygame import Surface
from pygame.draw import ellipse
from pygame.sprite import Sprite

from config import white
from game.direction import Direction


class Ball(Sprite):
    def __init__(self, color, radius):
        super().__init__()

        self.color = color
        self.radius = radius
        self.rx = 2
        self.ry = 2

        self.direction = Direction(0, 0)

        self.image = Surface((self.__width(), self.__height()))
        self.__draw_ball()
        self.rect = self.image.get_rect()

        self.restart()

    def restart(self):
        self.rect.x = 400
        self.rect.y = 300

        self.direction = Direction.random()

    def vertical_position(self):
        return self.rect.y

    def update(self):
        self.direction.update(self.rect)

    def __height(self):
        return self.radius * self.ry

    def __width(self):
        return self.radius * self.rx

    def __draw_ball(self):
        self.image.fill(white)
        self.image.set_colorkey(white)
        ellipse(self.image, self.color, [0, 0, self.__width(), self.__height()])

    def vertical_bounce(self):
        self.direction.vertical_bounce()

    def goal(self):
        self.restart()

    def bounce_with_pad(self, x_speed=1, y_speed=1):
        self.direction.horizontal_bounce(x_speed, y_speed)
