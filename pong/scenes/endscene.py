import pygame

import pong.config
from pong.config import styles
from pong.app.scene import Scene
from pong.app.window import Window


class EndScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        self.window.screen.fill(pong.config.black)
        self.window.score_board.final_board(self)
        self.text_renderer.blit('Press P to play again or any other key to exit', styles['prompt'])

        pygame.display.flip()
        done = False
        exit_code = 0

        pygame.event.clear()

        while not done:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == "p":
                    exit_code = self.window.PLAY_AGAIN
                done = True

        return exit_code
