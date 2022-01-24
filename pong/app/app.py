import pygame

from app.window import Window
from config import POINTS_TO_WIN, human_side, game_mode, width, height, title
from game.game import Game
from game.game_mode import GameMode
from game.scoring.match import Match
from game.scoring.score_manager import ScoreManager
from game.scoring.scoreboard import ScoreBoard
from game.side import Side
from scenes.endscene import EndScene
from scenes.gamescene import GameScene
from scenes.startscene import StartScene


class App(object):
    def __init__(self, match=Match(3, POINTS_TO_WIN)):
        self.window = Window(width, height, title)
        game = Game(Side.from_raw(human_side), GameMode.from_raw(game_mode))

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

        pygame.quit()
        return exit_code.value()

    def __add_scenes(self, *scenes):
        for scene in scenes:
            self.__add_scene(scene)

    def __add_scene(self, scene):
        self.window.add_scene(scene)
