import pygame

from pong.app.scene import Scene
from pong.app.window import Window
from pong.config import base_path, white, styles


class StartScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        self._show_background()

        done = False
        while not done:
            event = pygame.event.wait()
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key_name = pygame.key.name(event.key)
                if key_name == "r":
                    self._set_side_preference('right')
                elif key_name == 'l':
                    self._set_side_preference('left')
                elif key_name == '1':
                    self._set_game_mode(1)
                elif key_name == '2':
                    self._set_game_mode(2)
                else:
                    done = True

            self._show_background()
            self._show_configuration()
            self._show_press_key()

            pygame.display.flip()

        return 0

    def _show_press_key(self):
        self.text_renderer.blit('Press any key to play', styles['prompt'])

    def _set_game_mode(self, mode):
        self.window.set_mode(mode)

    def _set_side_preference(self, side):
        self.window.set_side(side)

    def _show_configuration(self):
        self.text_renderer.blit("Table side: L/R ({0}) ".format(self._game_side()), styles['config_side'])
        self.text_renderer.blit("Players: 1/2 ({0}) ".format(self._game_mode()), styles['config_players'])
        self._show_press_key()

    def _game_mode(self):
        return self.window.game_mode()

    def _game_side(self):
        return self.window.game_side()

    def _show_background(self):
        self.window.screen.fill(white)
        self.window.screen.blit(self._get_image_path(), (0, 0))

    @staticmethod
    def _get_image_path():
        return pygame.image.load(base_path + '/assets/pong.jpg')
