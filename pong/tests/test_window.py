import unittest.mock

from app.exit_code import ExitCode
from app.scene import Scene
from app.window import Window
from tests import events


class WindowTestCase(unittest.TestCase):
    @unittest.mock.patch('pygame.event.get', return_value=[events.quit_event, events.any_key_event])
    def test_should_run_fine(self, mock):
        window = Window(800, 600, 'title')
        self.assertTrue(window.run().equals(ExitCode.success()))

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
        with unittest.mock.patch.object(error_scene, 'run', wraps=error_scene.run, return_value=ExitCode(-1)):
            window.add_scene(error_scene)
            self.assertTrue(window.run().equals(ExitCode(-1)))

    def test_should_allow_play_again(self):
        window = Window(800, 600, 'Test')
        play_again_scene = Scene(window)
        with unittest.mock.patch.object(
                play_again_scene, 'run', wraps=play_again_scene.run,
                side_effect=[ExitCode.play_again(), ExitCode.success()]):
            window.add_scene(play_again_scene)
            self.assertTrue(window.run().equals(ExitCode.success()))


if __name__ == '__main__':
    unittest.main()
