from pygame.draw import ellipse
from pygame.sprite import Sprite

from field.positionable import Positionable
from game.direction import Direction
from utils.image import create_transparent_image


class Ball(Sprite, Positionable):
    def __init__(self, color, radius):
        super().__init__()

        self.color = color
        self.radius = radius
        self.rx = 2
        self.ry = 2

        self.direction = Direction(0, 0)

        self.image = self.__draw_ball()
        self.rect = self.image.get_rect()

        self.__restart()

    def update(self):
        self.direction.update(self.rect)

    def __height(self):
        return self.radius * self.ry

    def __width(self):
        return self.radius * self.rx

    def __draw_ball(self):
        image = create_transparent_image(self.__width(), self.__height())
        ellipse(image, self.color, [0, 0, self.__width(), self.__height()])
        return image

    def __restart(self):
        self.set_position(400, 300)

        self.direction = Direction.random()

    def vertical_bounce(self):
        self.direction.vertical_bounce()

    def goal(self):
        self.__restart()

    def bounce_with_pad(self, x_speed=1, y_speed=1):
        self.direction.horizontal_bounce(x_speed, y_speed)

    def y_center(self):
        return self.rect.y + self.radius
