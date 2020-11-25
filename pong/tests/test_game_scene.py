import unittest.mock

import pygame

import pong.scenes.gamescene
from app.window import Window
from tests import events


class GameSceneTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event])
    def test_should_run_fine(self, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = pong.scenes.gamescene.GameScene(window)

        pygame.init()
        self.assertEqual(0, scene.run())
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
