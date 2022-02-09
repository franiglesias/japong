import unittest.mock

import pygame

import pong.scenes.gamescene
from app.exit_code import ExitCode
from app.window import Window
from game.game import Game
from game.game_mode import OnePlayer
from game.side import Left
from tests import events


class GameSceneTestCase(unittest.TestCase):
    @unittest.mock.patch("pong.game.scoring.score_manager.ScoreManager")
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event])
    def test_should_run_fine(self, score_manager_mock, mock):
        window = Window(800, 600, 'Test')
        game = Game(Left(), OnePlayer())
        scene = pong.scenes.gamescene.GameScene(window, game, score_manager_mock)

        self.assertTrue(scene.run().equals(ExitCode.success()))
        self.tearDown()

    def setUp(self):
        pygame.display.init()
        pygame.font.init()

    def tearDown(self):
        pygame.display.quit()
        pygame.font.quit()


if __name__ == '__main__':
    unittest.main()
