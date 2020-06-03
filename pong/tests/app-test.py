import unittest

from pong.app.app import App


class AppTestCase(unittest.TestCase):
    def test_app_ran_fine(self):
        app = App()
        self.assertEqual(0, app.run())


if __name__ == '__main__':
    unittest.main()
