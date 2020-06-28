import unittest.mock

import pygame

import pong.scenes.startscene
from pong.app.window import Window
from pong.tests import events


class StartSceneTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.wait', return_value=events.any_key_event)
    def test_should_run_fine(self, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = pong.scenes.startscene.StartScene(window)

        pygame.init()
        self.assertEqual(0, scene.run())
        pygame.quit()

    @unittest.mock.patch('pygame.event.wait', side_effect=[events.r_key_event, events.any_key_event])
    def test_should_change_side_preference(self, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = pong.scenes.startscene.StartScene(window)

        pygame.init()
        scene.run()
        self.assertEqual('right', window.game.side_preference)
        pygame.quit()

    @unittest.mock.patch('pygame.event.wait', side_effect=[events.l_key_event, events.any_key_event])
    def test_should_change_side_preference(self, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = pong.scenes.startscene.StartScene(window)
        window.game.set_side_preference('right')
        pygame.init()
        scene.run()
        self.assertEqual('left', window.game.side_preference)
        pygame.quit()


if __name__ == '__main__':
    unittest.main()
