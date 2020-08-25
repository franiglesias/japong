import pygame
from pygame.sprite import Group
from pygame.time import Clock

import pong.config
from pong.app.scene import Scene
from pong.app.window import Window
from pong.ball import Ball
from pong.border import Border
from pong.config import POINTS_TO_WIN
from pong.game.control.computer_control_engine import ComputerControlEngine
from pong.game.control.keyboard_control_engine import KeyboardControlEngine
from pong.game.scoring.score_manager import ScoreManager
from pong.player import Player
from pong.scoreboard import ScoreBoard


class GameScene(Scene):
    def __init__(self, window: Window):
        super().__init__(window)
        self.all_sprites = Group()
        self.goals = Group()
        self.pads = Group()
        self.borders = Group()
        self.ball = Ball(pong.config.yellow, 10)
        self.all_sprites.add(self.ball)

    def run(self):

        self.prepare_borders()

        player_one_side = 'left'
        player_two_side = 'right'
        player_one_speed = self.window.game.human_speed
        player_two_speed = self.window.game.human_speed
        player_one_engine = self.player_engine(pong.config.left_keys)
        player_two_engine = self.player_engine(pong.config.right_keys)

        if self.window.game.game_mode == 1:
            player_one_side = self.window.game.side_preference
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

        self.window.score_manager = ScoreManager(player_one, player_two, (1, POINTS_TO_WIN))
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
        pygame.time.set_timer(pong.config.COMPUTER_MOVES_EVENT, pong.config.COMPUTER_MOVES_TIMER_MS)
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                player_one.handle(event)
                player_two.handle(event)

            pygame.event.pump()
            self.all_sprites.update()

            # Manage goals
            self.ball.manage_goals()

            # Game draw
            self.window.screen.fill(pong.config.green)
            self.window.score_board.draw(self)
            self.all_sprites.draw(self.window.screen)

            # Screen update
            pygame.display.flip()

            if self.window.score_manager.end_of_game():
                done = True

            clock.tick(pong.config.FPS)

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
