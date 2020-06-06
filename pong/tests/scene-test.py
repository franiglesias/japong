import unittest.mock

import pong.app.window
from pong.app.scene import Scene
from pong.scenes.ganescene import GameScene

class SceneTestCase(unittest.TestCase):
    def test_should_run_fine(self):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = Scene(window)
        self.assertEquals(0, scene.run())


if __name__ == '__main__':
    unittest.main()
