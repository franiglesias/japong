import pygame

from app.exit_code import ExitCode
from app.scene import Scene
from app.window import Window
from config import BASE_PATH, white, styles
from game.game import Game


class StartScene(Scene):
    def __init__(self, window: Window, game: Game):
        super().__init__(window)
        self.game = game

    def run(self):
        self._show_background()

        done = False
        while not done:
            event = pygame.event.wait()
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key_name = pygame.key.name(event.key)
                if key_name == "r":
                    self.game.prefer_right()
                elif key_name == 'l':
                    self.game.prefer_left()
                elif key_name == '1':
                    self.game.prefer_one_player()
                elif key_name == '2':
                    self.game.prefer_two_players()
                else:
                    done = True

            self._show_background()
            self._show_configuration()

            pygame.display.flip()

        return ExitCode.success()

    def _show_configuration(self):
        self.text_writer.a_line(
            "Table side: L/R ({0}) ".format(self.game.side_preference.str()),
            styles['config_side']
        )
        self.text_writer.a_line(
            "Players: 1/2 ({0}) ".format(self.game.game_mode.str()),
            styles['config_players']
        )
        self.text_writer.a_line(
            'Press any key to play',
            styles['prompt']
        )

    def _show_background(self):
        self.window.screen.fill(white)
        self.window.screen.blit(self._get_image_path(), (0, 0))

    @staticmethod
    def _get_image_path():
        return pygame.image.load(BASE_PATH + '/assets/pong.jpg')
