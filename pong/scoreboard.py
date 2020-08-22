import pong.config
from pong.config import POINTS_TO_WIN


class ScoreBoard:
    def __init__(self, player_one, player_two):
        if player_one.side == 'left':
            self.left = player_one
            self.right = player_two
        else:
            self.left = player_two
            self.right = player_one

        self.target = POINTS_TO_WIN

    def draw(self, scene):
        board = self.score()
        scene.text_renderer.blit(board, pong.config.style_score)

    def score(self):
        return " {0} : {1} ".format(self.left.score(), self.right.score())

    def end_of_game(self):
        return self.left.score() == self.target or self.right.score() == self.target

    def winner(self, scene):
        board = self.final_board()
        scene.text_renderer.blit(board, pong.config.style_score)

    def final_board(self):
        if self.left.score() > self.right.score():
            winner = self.left
        else:
            winner = self.right
        score = self.score()
        return (" {0} WON!" + score).format(winner.name)
