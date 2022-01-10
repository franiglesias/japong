import pygame
from pygame.sprite import Group
from pygame.time import Clock

from app.exit_code import ExitCode
from app.scene import Scene
from app.window import Window
from config import COMPUTER_MOVES_EVENT, FPS, COMPUTER_MOVES_TIMER_MS
from config import yellow, green
from field.border import Border
from field.goal import Goal
from field.net import Net
from game.ball import Ball
from game.control.computer_control_engine import ComputerControlEngine
from game.control.keyboard_control_engine import KeyboardControlEngine
from game.game import Game
from game.pad import Pad
from game.scoring.score_manager import ScoreManager
from game.scoring.scoreboard import ScoreBoard


class GameScene(Scene):
    def __init__(self, window: Window, game: Game, score_manager: ScoreManager, score_board: ScoreBoard):
        super().__init__(window)

        self.game = game
        self.score_manager = score_manager

        self.ball = Ball(yellow, 10)
        self.game.game_mode.bind_ball(self.ball)

        self.all_sprites = Group()
        self.goals = Group()
        self.pads = Group()

        self.borders = Group()

        self.all_sprites.add(Net())
        self.all_sprites.add(self.ball)

        self.player_one = self.game.player_one()
        self.player_two = self.game.player_two()

        self.score_manager.register_players(self.player_one, self.player_two)
        self.score_board = score_board

    def run(self):

        self.__prepare_borders()

        self.player_one.pad.borders = self.borders
        self.player_two.pad.borders = self.borders

        self.goals.add(self.player_one.goal)
        self.goals.add(self.player_two.goal)

        self.pads.add(self.player_one.pad)
        self.pads.add(self.player_two.pad)

        goal: Goal
        for goal in self.goals:
            goal.bind_ball(self.ball)
            self.all_sprites.add(goal)

        pad: Pad
        for pad in self.pads:
            pad.bind_ball(self.ball)
            self.all_sprites.add(pad)

        # Game loop
        clock = Clock()
        pygame.time.set_timer(COMPUTER_MOVES_EVENT, COMPUTER_MOVES_TIMER_MS)
        end_of_match = False

        while not end_of_match:

            end_of_set = False
            while not end_of_set:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end_of_match = True
                        break
                    self.player_one.handle(event)
                    self.player_two.handle(event)

                pygame.event.pump()
                self.all_sprites.update()

                # Game draw
                self.window.screen.fill(green)
                self.score_board.draw(self)
                self.all_sprites.draw(self.window.screen)

                # Screen update
                pygame.display.flip()

                if self.score_manager.end_of_set():
                    end_of_set = True
                    self.score_manager.end_set()
                    self.score_manager.new_set()

                    if self.score_manager.end_of_game():
                        end_of_match = True

                clock.tick(FPS)
        return ExitCode.success()

    def player_engine(self, keys):
        if len(keys) == 0:
            return ComputerControlEngine(self.ball)

        return KeyboardControlEngine(keys)

    def __prepare_borders(self):
        self.borders.add(Border(0))
        self.borders.add(Border(590))

        border: Border
        for border in self.borders:
            border.bind_ball(self.ball)
            self.all_sprites.add(border)
