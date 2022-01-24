import unittest

from game.game import Game
from game.game_mode import OnePlayer
from game.side import Left, Right


class GameTestCase(unittest.TestCase):
    def test_should_allow_to_set_side_preference(self):
        game = Game(Left(), OnePlayer())
        game.prefer_right()
        self.assertTrue(Right().equals(game.side_preference))
        game.prefer_left()
        self.assertTrue(Left().equals(game.side_preference))


if __name__ == '__main__':
    unittest.main()
