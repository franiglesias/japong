import pygame

from app.window import Window
from game.game import Game
from game.game_mode import GameMode
from game.scoring.score_manager import ScoreManager
from game.side import Side
from scenes.endscene import EndScene
from scenes.gamescene import GameScene
from scenes.startscene import StartScene
from utils.configuration import read_configuration


class App:
    def __init__(self, match):
        screen = read_configuration('screen')
        self.window = Window(screen.getint('width'), screen.getint('height'), screen['title'])

        prefs = read_configuration('preferences')
        game = Game(Side.from_raw(prefs['human_side']), GameMode.from_raw(prefs['game_mode']))

        score_manager = ScoreManager(match)

        self.__add_scenes(
            StartScene(self.window, game),
            GameScene(self.window, game, score_manager),
            EndScene(self.window, score_manager)
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
