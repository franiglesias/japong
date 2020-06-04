import unittest.mock

from pong.app.app import App
from pong.tests import events


class AppTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event, events.any_key_event])
    def test_app_ran_fine(self, mock):
        app = App()
        self.assertEqual(0, app.run())


if __name__ == '__main__':
    unittest.main()
