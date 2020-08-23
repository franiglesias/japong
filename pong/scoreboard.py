import pong.config
from pong.game.scoring.score_manager import ScoreManager


class ScoreBoard:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def draw(self, scene):
        board = self.score()
        scene.text_renderer.blit(board, pong.config.style_score)

    def score(self):
        return " {0} : {1} ".format(self.score_manager.score()[0], self.score_manager.score()[1])

    def end_of_game(self):
        return self.score_manager.end_of_game()

    def winner(self, scene):
        board = self.final_board()
        scene.text_renderer.blit(board, pong.config.style_score)

    def final_board(self):
        winner = self.score_manager.winner()

        score = self.score()
        return (" {0} WON!" + score).format(winner.name)
