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
from game.game import Game
from game.pad import Pad
from game.scoring.score_manager import ScoreManager
from game.scoring.scoreboard import ScoreBoard


class GameScene(Scene):
    def __init__(
            self,
            window: Window,
            game: Game,
            score_manager: ScoreManager,
    ):
        super().__init__(window)
        self.score_manager = score_manager
        self.game = game
        self.score_board = ScoreBoard(score_manager)
        self.pads = Group()

    def run(self):
        all_sprites = self.__prepare_game()

        return self.__game_loop(all_sprites)

    def __prepare_game(self):
        ball = Ball(yellow, 10)
        self.game.game_mode.bind_ball(ball)

        pad_one, player_one = self.game.game_mode.player_one()
        pad_two, player_two = self.game.game_mode.player_two()

        self.score_manager.register_players(player_one, player_two)

        borders = Group()
        borders.add(Border(0, 0, 800, 10))
        borders.add(Border(0, 590, 800, 10))

        pad_one.borders = borders
        pad_two.borders = borders

        goals = Group()
        goals.add(Goal(player_one))
        goals.add(Goal(player_two))

        self.pads.add(pad_one)
        self.pads.add(pad_two)

        border: Border
        for border in borders:
            border.bind_ball(ball)

        goal: Goal
        for goal in goals:
            goal.bind_ball(ball)

        pad: Pad
        for pad in self.pads:
            pad.bind_ball(ball)

        return self.collect_sprites(ball, borders, goals, self.pads)

    def __game_loop(self, all_sprites):
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
                    pad: Pad
                    for pad in self.pads:
                        pad.handle(event)

                pygame.event.pump()
                all_sprites.update()

                # Game draw
                self.window.screen.fill(green)
                self.score_board.draw(self)
                all_sprites.draw(self.window.screen)

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

    def collect_sprites(self, ball, borders, goals, pads):
        all_sprites = Group()
        all_sprites.add(Net())
        all_sprites.add(ball)
        border: Border
        for border in borders:
            all_sprites.add(border)
        goal: Goal
        for goal in goals:
            all_sprites.add(goal)
        pad: Pad
        for pad in pads:
            all_sprites.add(pad)
        return all_sprites
