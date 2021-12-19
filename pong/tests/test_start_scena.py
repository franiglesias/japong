import unittest.mock

import pygame

from app.exit_code import ExitCode
from app.window import Window
from game.game import Game
from scenes.startscene import StartScene
from tests import events


class StartSceneTestCase(unittest.TestCase):
    def setUp(self) -> None:
        window = Window(800, 600, 'Test')
        self.game = Game()
        self.scene = StartScene(window, self.game)
        pygame.init()

    def tearDown(self) -> None:
        pygame.quit()

    @unittest.mock.patch('pygame.event.wait', return_value=events.any_key_event)
    def test_should_run_fine(self, mock):
        self.assertTrue(self.scene.run().equals(ExitCode.success()))

    @unittest.mock.patch('pygame.event.wait', side_effect=[events.r_key_event, events.any_key_event])
    def test_r_key_should_change_side_preference_to_right(self, mock):
        self.game.prefer_left()
        self.scene.run()
        self.assertEqual('right', self.game.side_preference)

    @unittest.mock.patch('pygame.event.wait', side_effect=[events.l_key_event, events.any_key_event])
    def test_l_key_should_change_side_preference_to_left(self, mock):
        self.game.prefer_right()
        self.scene.run()
        self.assertEqual('left', self.game.side_preference)

    @unittest.mock.patch('pygame.event.wait', side_effect=[events.num_1_key_event, events.any_key_event])
    def test_1_key_should_change_game_mode_to_single_player(self, mock):
        self.game.prefer_two_players()
        self.scene.run()
        self.assertEqual(1, self.game.game_mode)

    @unittest.mock.patch('pygame.event.wait', side_effect=[events.num_2_key_event, events.any_key_event])
    def test_2_key_should_change_game_mode_to_two_players(self, mock):
        self.game.prefer_one_player()
        self.scene.run()
        self.assertEqual(2, self.game.game_mode)


if __name__ == '__main__':
    unittest.main()
