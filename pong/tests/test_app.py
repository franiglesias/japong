import unittest.mock

from app.app import App
from game.scoring.match import Match
from tests import events


class AppTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.wait', return_value=events.any_key_event)
    @unittest.mock.patch('pygame.event.get', return_value=[events.any_key_event, events.quit_event])
    def test_app_can_run(self, pass_start_scene, pass_end_scene):
        app = App(Match(1, 1, 1))
        self.assertEqual(0, app.run())


if __name__ == '__main__':
    unittest.main()
