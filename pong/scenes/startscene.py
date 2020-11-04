import pygame

from pong.app.scene import Scene
from pong.app.window import Window
from pong.config import base_path, white, style_prompt, style_config_side, style_config_players


class StartScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        image = pygame.image.load(base_path + '/assets/pong.jpg')

        self.window.screen.fill(white)
        self.window.screen.blit(image, (0, 0))
        self.text_renderer.blit('Press any key to play', style_prompt)

        done = False
        while not done:
            event = pygame.event.wait()
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key_name = pygame.key.name(event.key)
                if key_name == "r":
                    self.window.game.set_side_preference('right')
                elif key_name == 'l':
                    self.window.game.set_side_preference('left')
                elif key_name == '1':
                    self.window.game.set_game_mode(1)
                elif key_name == '2':
                    self.window.game.set_game_mode(2)
                else:
                    done = True

            self.window.screen.fill(white)
            self.window.screen.blit(image, (0, 0))
            self.text_renderer.blit("Table side: L/R ({0}) ".format(self.window.game.side_preference),
                                    style_config_side)
            self.text_renderer.blit("Players: 1/2 ({0}) ".format(self.window.game.game_mode), style_config_players)
            self.text_renderer.blit('Press any key to play', style_prompt)

            pygame.display.flip()

        return 0
