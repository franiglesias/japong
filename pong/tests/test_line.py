from unittest import TestCase

import pygame.font
from pygame import Surface
from pygame.font import Font, get_default_font

from config import black, white
from utils.line import Position


class TestLine(TestCase):
    def setUp(self) -> None:
        pygame.font.init()
        the_font = Font(get_default_font(), 20)

        self.text = the_font.render('Example', False, black, white)
        self.surface = Surface((100, 100))

    def tearDown(self) -> None:
        pygame.font.quit()

    def test_position_from_style(self):
        position = Position.from_style('left', 'top', self.text, self.surface)

        self.assertEqual((30, 30), position.coordinates())

    def test_from_coordinates(self):
        position = Position.from_style(40, 15, self.text, self.surface)

        self.assertEqual((40, 15), position.coordinates())

    def test_mixed_definition(self):
        position = Position.from_style('left', 5, self.text, self.surface)

        self.assertEqual((30, 5), position.coordinates())
