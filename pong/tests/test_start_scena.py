import unittest.mock

import pygame

import pong.scenes.startscene
from pong.app.window import Window
from pong.tests import events


class StartSceneTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.any_key_event])
    def test_should_run_fine(self, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = pong.scenes.startscene.StartScene(window)

        pygame.init()
        self.assertEqual(0, scene.run())
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
