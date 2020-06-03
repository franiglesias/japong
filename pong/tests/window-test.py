import unittest

from pong.app.window import Window


class WindowTestCase(unittest.TestCase):
    def test_should_run_fine(self):
        window = Window(800, 600, 'title')
        self.assertEqual(0, window.run())


if __name__ == '__main__':
    unittest.main()
