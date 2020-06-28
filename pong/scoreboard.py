import pygame

import pong.config
from pong.config import POINTS_TO_WIN


class ScoreBoard:
    def __init__(self, left_player, right_player):
        self.left_player = left_player
        self.right_player = right_player
        self.target = POINTS_TO_WIN

    def draw(self, scene):
        board = self.score()
        scene.text_renderer.blit(board, pong.config.style_score)

    def score(self):
        return " {0} : {1} ".format(self.left_player.score, self.right_player.score)

    def stop(self):
        return self.left_player.score == self.target or self.right_player.score == self.target

    def winner(self, scene):
        board = self.final_board()
        scene.text_renderer.blit(board, pong.config.style_score)

    def final_board(self):
        if self.left_player.score > self.right_player.score:
            winner = self.left_player
        else:
            winner = self.right_player
        score = self.score()
        return (" {0} WON!" + score).format(winner.name)
