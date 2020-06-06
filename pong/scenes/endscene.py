import pygame

import pong.config
from pong.app.scene import Scene
from pong.app.window import Window


class EndScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        self.window.score_board.winner(self.window.screen)

        self.text_renderer.blit(pong.config.text_main_title, 'Game finished', 'center', 'middle')
        self.text_renderer.blit(pong.config.text_prompt, 'Press any key to exit', 'center', 'bottom')

        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True

        return 0
