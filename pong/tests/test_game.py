import unittest

from game.game import Game


class GameTestCase(unittest.TestCase):
    def test_should_allow_to_set_side_preference(self):
        game = Game()
        game.prefer_right()
        self.assertEqual('right', game.side_preference)
        game.prefer_left()
        self.assertEqual('left', game.side_preference)


if __name__ == '__main__':
    unittest.main()
