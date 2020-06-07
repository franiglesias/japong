import pygame

import pong.config
from pong.config import POINTS_TO_WIN


class ScoreBoard:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.target = POINTS_TO_WIN

    def draw(self, scene):
        board = " {0} : {1} ".format(self.player1.score, self.player2.score)
        scene.text_renderer.blit(board, pong.config.style_score)

    def stop(self):
        return self.player1.score == self.target or self.player2.score == self.target

    def winner(self, scene):
        if self.player1.score > self.player2.score:
            winner = self.player1
        else:
            winner = self.player2
        board = " {0} WON! ({1}-{2}) ".format(winner.name, self.player1.score, self.player2.score)
        scene.text_renderer.blit(board, pong.config.style_score)
