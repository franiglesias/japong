from unittest import TestCase

from game.score import Score


class TestScore(TestCase):
    def setUp(self):
        self.score = Score()

    def test_it_adds_points(self):
        self.score.win_point()
        self.assertEqual(1, self.score.points())

    def test_it_adds_sets(self):
        self.score.win_set()
        self.assertEqual(1, self.score.sets())

    def test_it_group_points_in_sets(self):
        self.score.new_set()
        self.assertEqual([0], self.score.partials())

    def test_simulate_a_game(self):
        self.win_many_points(3)
        self.score.new_set()
        self.win_many_points(5)
        self.score.end_match()
        self.assertEqual([3, 5], self.score.partials())

    def win_many_points(self, qty):
        for i in range(qty):
            self.score.win_point()
