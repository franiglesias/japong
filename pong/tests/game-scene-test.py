import unittest.mock

import pong.scenes.gamescene
from pong.app.window import Window
from pong.tests import events


class GameSceneTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event])
    def test_should_run_fine(self, mock):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = pong.scenes.gamescene.GameScene(window)

        self.assertEqual(0, scene.run())


if __name__ == '__main__':
    unittest.main()
