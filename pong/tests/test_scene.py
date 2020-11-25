import unittest.mock

import pong.app.window
from app.scene import Scene


class SceneTestCase(unittest.TestCase):
    def test_should_run_fine(self):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = Scene(window)
        self.assertEqual(0, scene.run())


if __name__ == '__main__':
    unittest.main()
