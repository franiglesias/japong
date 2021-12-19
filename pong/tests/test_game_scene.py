import unittest.mock

import pygame

import pong.scenes.gamescene
from app.exit_code import ExitCode
from app.window import Window
from tests import events


class GameSceneTestCase(unittest.TestCase):
    @unittest.mock.patch("pong.game.scoring.score_manager.ScoreManager")
    @unittest.mock.patch("pong.game.scoring.scoreboard.ScoreBoard")
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event])
    def test_should_run_fine(self, score_manager_mock, score_board_mock, mock):
        window = Window(800, 600, 'Test')

        scene = pong.scenes.gamescene.GameScene(window, score_manager_mock, score_board_mock)

        pygame.init()
        self.assertTrue(scene.run().equals(ExitCode.success()))
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
