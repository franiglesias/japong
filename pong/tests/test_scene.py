import unittest.mock

import pong.app.window
from app.exit_code import ExitCode
from app.scene import Scene


class SceneTestCase(unittest.TestCase):
    def test_should_run_fine(self):
        window = pong.app.window.Window(800, 600, 'Test')
        scene = Scene(window)
        self.assertTrue(scene.run().equals(ExitCode.success()))


if __name__ == '__main__':
    unittest.main()
