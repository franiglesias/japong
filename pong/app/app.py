import pygame

from app.window import Window
from config import HUMAN_SIDE, GAME_MODE, WIDTH, HEIGHT, TITLE
from game.game import Game
from game.game_mode import GameMode
from game.scoring.score_manager import ScoreManager
from game.scoring.scoreboard import ScoreBoard
from game.side import Side
from scenes.endscene import EndScene
from scenes.gamescene import GameScene
from scenes.startscene import StartScene


class App:
    def __init__(self, match):
        self.window = Window(WIDTH, HEIGHT, TITLE)
        game = Game(Side.from_raw(HUMAN_SIDE), GameMode.from_raw(GAME_MODE))

        score_manager = ScoreManager(match)
        score_board = ScoreBoard(score_manager)

        self.__add_scenes(
            StartScene(self.window, game),
            GameScene(self.window, game, score_manager, score_board),
            EndScene(self.window, score_board)
        )

    def run(self):
        pygame.display.init()
        pygame.font.init()
        exit_code = self.window.run()

        pygame.display.quit()
        pygame.font.quit()
        return exit_code.value()

    def __add_scenes(self, *scenes):
        for scene in scenes:
            self.window.add_scene(scene)
