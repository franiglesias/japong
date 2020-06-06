import pygame

import pong.utils.textrenderer
import pong.config
from pong.app.scene import Scene
from pong.app.window import Window


class StartScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        image = pygame.image.load(pong.config.basepath + '/assets/pong.jpg')

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True

            self.window.screen.fill(pong.config.white)

            self.window.screen.blit(image, (0, 0))
            self.text_renderer.blit(pong.config.text_prompt, 'Press any key to play', 'center', 'bottom')

            pygame.display.flip()

        return 0
