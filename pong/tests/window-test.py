import unittest.mock

from pong.app.window import Window
from pong.tests import events


class WindowTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event, events.any_key_event])
    def test_should_run_fine(self, mock):
        window = Window(800, 600, 'title')
        self.assertEqual(0, window.run())


if __name__ == '__main__':
    unittest.main()
