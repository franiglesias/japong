from unittest import TestCase

import pong.config
from pong.game.ball import Ball
from pong.game.control.computer_control_engine import ComputerControlEngine
from pong.game.scoring.score_manager import ScoreManager
from pong.game.player import Player


class TestScoreManager(TestCase):
    def testLeftPlayerWinsSet(self):
        self.scoreAfterSet(5, 0)
        self.assertEqual(self.left_player, self.score_manager.winner())

    def testShouldNotWinASetIfMinimumPointsNotReached(self):
        self.scoreAfterSet(4, 0)
        self.assertFalse(self.score_manager.end_of_set())

    def testShouldWinASetByTwoOrMorePoints(self):
        self.scoreAfterSet(5, 0)
        self.assertTrue(self.score_manager.end_of_set())
        self.scoreAfterSet(5, 3)
        self.assertTrue(self.score_manager.end_of_set())
        self.scoreAfterSet(7, 5)
        self.assertTrue(self.score_manager.end_of_set())

    def testShouldNotWinSetIfNoEnoughDifference(self):
        self.scoreAfterSet(5, 4)
        self.assertFalse(self.score_manager.end_of_set())
        self.scoreAfterSet(6, 5)
        self.assertFalse(self.score_manager.end_of_set())
        self.scoreAfterSet(7, 6)
        self.assertFalse(self.score_manager.end_of_set())

    def testShouldEndGame(self):
        self.scoreInSets(2, 0)
        self.assertTrue(self.score_manager.end_of_game())
        self.scoreInSets(2, 1)
        self.assertTrue(self.score_manager.end_of_game())
        self.scoreInSets(3, 0)
        self.assertTrue(self.score_manager.end_of_game())

    def test_should_not_end_game(self):
        self.scoreInSets(0, 0)
        self.assertFalse(self.score_manager.end_of_game())
        self.scoreInSets(1, 1)
        self.assertFalse(self.score_manager.end_of_game())
        self.scoreInSets(1, 0)
        self.assertFalse(self.score_manager.end_of_game())

    def test_one_set_match_should_have_only_one_set(self):
        self.left_player = self.preparePlayer()
        self.right_player = self.preparePlayer()
        self.score_manager = ScoreManager(self.left_player, self.right_player, (1, 5))
        self.left_player.win_set()
        self.assertTrue(self.score_manager.end_of_game())

    def scoreAfterSet(self, left, right):
        self.left_player = self.preparePlayer()
        self.right_player = self.preparePlayer()
        for i in range(left):
            self.left_player.win_point()
        for i in range(right):
            self.right_player.win_point()
        self.score_manager = ScoreManager(self.left_player, self.right_player, (3, 5))

    def scoreInSets(self, left, right):
        self.left_player = self.preparePlayer()
        self.right_player = self.preparePlayer()
        for i in range(left):
            self.left_player.win_set()
        for i in range(right):
            self.right_player.win_set()
        self.score_manager = ScoreManager(self.left_player, self.right_player, (3, 5))

    @staticmethod
    def preparePlayer():
        ball = Ball(pong.config.white, 10)
        engine = ComputerControlEngine(ball)
        return Player('left', 'left', engine)
