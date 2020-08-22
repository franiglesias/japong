from unittest import TestCase

from pong.game.score import Score


class TestScore(TestCase):
    def setUp(self):
        self.score = Score()

    def test_it_adds_points(self):
        self.score.win_point()
        self.assertEqual(1, self.score.points())

    def test_it_adds_sets(self):
        self.score.new_set()
        self.assertEqual(0, self.score.points())
        self.assertEqual([0], self.score.score())

    def test_simulate_a_game(self):
        self.win_many_points(3)
        self.score.new_set()
        self.win_many_points(5)
        self.score.end_match()
        self.assertEqual([3, 5], self.score.score())

    def win_many_points(self, qty):
        for i in range(qty):
            self.score.win_point()
