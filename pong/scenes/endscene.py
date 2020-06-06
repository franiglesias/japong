import pygame

import pong.config
from pong.app.scene import Scene
from pong.app.window import Window


class EndScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        scoreFont = pygame.font.Font(pygame.font.get_default_font(), 64)
        text = scoreFont.render('Game finished', True, pong.config.yellow, pong.config.green)
        self.window.score_board.winner(self.window.screen)
        text_rect = text.get_rect()
        text_rect.center = (800 // 2, 600 // 2)
        self.window.screen.blit(text, text_rect)
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    done = True

        return 0
