import pygame

from config import styles
from config import black
from app.scene import Scene
from app.window import Window
from app.exit_code import ExitCode


class EndScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)

    def run(self):
        self.window.screen.fill(black)
        self.window.score_board.final_board(self)
        self.text_renderer.blit('Press P to play again or any other key to exit', styles['prompt'])

        pygame.display.flip()
        done = False
        exit_code = ExitCode.success()

        pygame.event.clear()

        while not done:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == "p":
                    exit_code = ExitCode.play_again()
                done = True

        return exit_code
