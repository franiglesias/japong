import unittest

from game.game import Game


class GameTestCase(unittest.TestCase):
    def test_should_allow_to_set_side_preference(self):
        game = Game()
        game.set_side_preference('right')
        self.assertEqual('right', game.side_preference)


if __name__ == '__main__':
    unittest.main()
