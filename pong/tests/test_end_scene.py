import unittest.mock

import pygame

import pong.scenes.endscene
from pong.app.window import Window
from pong.tests import events


class EndSceneTestCase(unittest.TestCase):
    @unittest.mock.patch("pong.scoreboard.ScoreBoard")
    @unittest.mock.patch('pygame.event.get', return_value=[events.any_key_event])
    def test_should_run_fine(self, score_board_mock, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        window.score_board = score_board_mock
        scene = pong.scenes.endscene.EndScene(window)

        pygame.init()
        self.assertEqual(0, scene.run())
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
