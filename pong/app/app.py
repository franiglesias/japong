import pygame

from app.window import Window
from config import POINTS_TO_WIN
from game.game import Game
from game.scoring.match import Match
from game.scoring.score_manager import ScoreManager
from game.scoring.scoreboard import ScoreBoard
from scenes.endscene import EndScene
from scenes.gamescene import GameScene
from scenes.startscene import StartScene


class App(object):
    def __init__(self):
        self.window = Window(800, 600, 'Japong!')
        game = Game()
        score_manager = ScoreManager(Match(3, POINTS_TO_WIN))
        score_board = ScoreBoard(score_manager)
        self.add_scene(StartScene(self.window, game))
        self.add_scene(GameScene(self.window, game, score_manager, score_board))
        self.add_scene(EndScene(self.window, score_board))

    def run(self):
        pygame.init()
        code = self.window.run()

        pygame.quit()
        return code

    def add_scene(self, scene):
        self.window.add_scene(scene)
