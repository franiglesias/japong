import pygame

import pong.config
from pong.app.scene import Scene
from pong.app.window import Window


class EndScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        self.window.score_board.winner(self)

        self.text_renderer.blit('Game finished', pong.config.style_end_title)
        self.text_renderer.blit('Press any key to exit', pong.config.style_prompt)

        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True

        return 0
