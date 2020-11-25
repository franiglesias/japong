import pygame
from pygame.sprite import Group
from pygame.time import Clock

from config import yellow, green
from config import COMPUTER_MOVES_EVENT, FPS, COMPUTER_MOVES_TIMER_MS
from config import left_keys, right_keys
from field.net import Net
from app.scene import Scene
from app.window import Window
from game.ball import Ball
from field.border import Border
from config import POINTS_TO_WIN
from game.control.computer_control_engine import ComputerControlEngine
from game.control.keyboard_control_engine import KeyboardControlEngine
from game.scoring.score_manager import ScoreManager
from game.player import Player
from game.scoring.scoreboard import ScoreBoard


class GameScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)
        self.all_sprites = Group()
        self.goals = Group()
        self.pads = Group()
        self.borders = Group()
        self.ball = Ball(yellow, 10)
        self.all_sprites.add(Net())
        self.all_sprites.add(self.ball)

    def run(self):

        self.prepare_borders()

        player_one_side = 'left'
        player_two_side = 'right'
        player_one_speed = self.window.game.human_speed
        player_two_speed = self.window.game.human_speed
        player_one_engine = self.player_engine(left_keys)
        player_two_engine = self.player_engine(right_keys)

        if self.window.game.game_mode == 1:
            player_one_side = self.window.game_side()
            if player_one_side == 'left':
                player_two_side = 'right'
            else:
                player_two_side = 'left'
            player_one_speed = self.window.game.human_speed
            player_two_speed = self.window.game.computer_speed
            player_two_engine = self.player_engine(())
        elif self.window.game.game_mode == 0:
            player_one_speed = self.window.game.computer_speed
            player_two_speed = self.window.game.computer_speed
            player_one_engine = self.player_engine(())
            player_two_engine = self.player_engine(())

        player_one = Player('human', player_one_side, player_one_engine, player_one_speed)
        player_two = Player('computer', player_two_side, player_two_engine, player_two_speed)

        self.window.score_manager = ScoreManager(
            match=(3, POINTS_TO_WIN),
            player_one=player_one,
            player_two=player_two
        )
        self.window.score_board = ScoreBoard(self.window.score_manager)

        player_one.pad.borders = self.borders
        player_two.pad.borders = self.borders

        self.all_sprites.add(player_one.goal)
        self.all_sprites.add(player_two.goal)

        self.goals.add(player_one.goal)
        self.goals.add(player_two.goal)

        self.all_sprites.add(player_one.pad)
        self.all_sprites.add(player_two.pad)

        self.pads.add(player_one.pad)
        self.pads.add(player_two.pad)

        self.ball.pads = self.pads
        self.ball.borders = self.borders
        self.ball.goals = self.goals

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
                    player_one.handle(event)
                    player_two.handle(event)

                pygame.event.pump()
                self.all_sprites.update()

                # Manage goals
                self.ball.manage_goals()

                # Game draw
                self.window.screen.fill(green)
                self.window.score_board.draw(self)
                self.all_sprites.draw(self.window.screen)

                # Screen update
                pygame.display.flip()

                if self.window.score_manager.end_of_set():
                    end_of_set = True
                    self.window.score_manager.end_set()
                    self.window.score_manager.new_set()

                    if self.window.score_manager.end_of_game():
                        end_of_match = True

                clock.tick(FPS)
        return 0

    def player_engine_for_second_player(self, keys):
        if self.window.game.game_mode == 1 or self.window.game.game_mode == 0:
            return ComputerControlEngine(self.ball)

        return KeyboardControlEngine(keys)

    def player_engine(self, keys):
        if len(keys) == 0:
            return ComputerControlEngine(self.ball)

        return KeyboardControlEngine(keys)

    def prepare_borders(self):
        border_top = Border(0)
        border_bottom = Border(590)
        self.all_sprites.add(border_top)
        self.all_sprites.add(border_bottom)
        self.borders.add(border_top)
        self.borders.add(border_bottom)
