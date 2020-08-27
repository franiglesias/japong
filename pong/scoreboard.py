import pong.config


class ScoreBoard:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def draw(self, scene):
        scene.text_renderer.blit(self.points(), pong.config.style_score)
        scene.text_renderer.blit(self.sets(), pong.config.style_sets)

    def points(self):
        return "{0} : {1}".format(
            self.score_manager.score()[0],
            self.score_manager.score()[1],
        )

    def sets(self):
        return "{0} : {1}".format(
            self.score_manager.sets()[0],
            self.score_manager.sets()[1],
        )

    def end_of_game(self):
        return self.score_manager.end_of_game()

    def winner(self, scene):
        board = self.final_board()
        scene.text_renderer.blit(board, pong.config.style_score)

    def final_board(self):
        winner = self.score_manager.winner()

        score = self.points()
        return (" {0} WON!" + score).format(winner.name)
