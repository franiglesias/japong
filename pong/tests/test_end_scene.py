import unittest.mock

import pygame

from app.exit_code import ExitCode
from app.window import Window
from scenes.endscene import EndScene
from tests import events


class EndSceneTestCase(unittest.TestCase):
    @unittest.mock.patch("pong.game.scoring.scoreboard.ScoreBoard")
    @unittest.mock.patch('pygame.event.wait', return_value=events.any_key_event)
    def test_should_run_fine(self, score_board_mock, mock):
        window = Window(800, 600, 'Test')
        window.score_board = score_board_mock
        scene = EndScene(window, score_board_mock)

        pygame.init()
        self.assertTrue(scene.run().equals(ExitCode.success()))
        pygame.quit()

    @unittest.mock.patch("pong.game.scoring.scoreboard.ScoreBoard")
    @unittest.mock.patch('pygame.event.wait', return_value=events.p_key_event)
    def test_should_ask_play_again_when_pressing_p(self, score_board_mock, mock):
        window = Window(800, 600, 'Test')
        window.score_board = score_board_mock
        scene = EndScene(window, score_board_mock)

        pygame.init()
        self.assertTrue(scene.run().equals(ExitCode.play_again()))
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
