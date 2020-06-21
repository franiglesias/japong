import unittest.mock

from pong.app.scene import Scene
from pong.app.window import Window
from pong.tests import events


class WindowTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event, events.any_key_event])
    def test_should_run_fine(self, mock):
        window = Window(800, 600, 'title')
        self.assertEqual(0, window.run())

    def test_should_add_scenes(self):
        window = Window(800, 600, 'Test')
        window.add_scene(Scene(window))
        self.assertEqual(1, len(window.scenes))

    def test_should_run_scenes(self):
        window = Window(800, 600, 'Test')
        scene = Scene(window)
        with unittest.mock.patch.object(scene, 'run', wraps=scene.run) as spy:
            window.add_scene(scene)
            window.run()
            spy.assert_called()

    def test_should_exit_with_error(self):
        window = Window(800, 600, 'Test')
        error_scene = Scene(window)
        with unittest.mock.patch.object(error_scene, 'run', wraps=error_scene.run, return_value=-1) as spy:
            window.add_scene(error_scene)
            self.assertEqual(-1, window.run())

    def test_should_allow_play_again(self):
        window = Window(800, 600, 'Test')
        play_again_scene = Scene(window)
        with unittest.mock.patch.object(play_again_scene, 'run', wraps=play_again_scene.run, side_effect=[1, 0]) as spy:
            window.add_scene(play_again_scene)
            self.assertEqual(0, window.run())


if __name__ == '__main__':
    unittest.main()
