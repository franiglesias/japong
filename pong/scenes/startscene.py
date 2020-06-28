import pygame

import pong.config
import pong.utils.textrenderer
from pong.app.scene import Scene
from pong.app.window import Window


class StartScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        image = pygame.image.load(pong.config.basepath + '/assets/pong.jpg')

        self.window.screen.fill(pong.config.white)

        self.window.screen.blit(image, (0, 0))
        self.text_renderer.blit('Press any key to play', pong.config.style_prompt)

        done = False
        while not done:
            event = pygame.event.wait()
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                key_name = pygame.key.name(event.key)
                if key_name == "r":
                    self.window.game.set_side_preference('right')
                elif key_name == 'l':
                    self.window.game.set_side_preference('left')
                else:
                    done = True

            self.window.screen.fill(pong.config.white)
            self.window.screen.blit(image, (0, 0))
            self.text_renderer.blit('Press any key to play', pong.config.style_prompt)
            self.text_renderer.blit("Table side: L/R ({0}) ".format(self.window.game.side_preference), pong.config.style_config)

            pygame.display.flip()

        return 0
