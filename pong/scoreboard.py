import pong.config


class ScoreBoard:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.target = 5

    def draw(self, in_screen):
        from pong.main import scoreFont
        board = " {0} : {1} ".format(self.player1.score, self.player2.score)
        score_text = scoreFont.render(board, True, pong.config.black, pong.config.white)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (800 // 2, 40)
        in_screen.blit(score_text, score_text_rect)

    def stop(self):
        return self.player1.score == self.target or self.player2.score == self.target

    def winner(self, in_screen):
        if self.player1.score > self.player2.score:
            winner = self.player1
        else:
            winner = self.player2
        from pong.main import scoreFont

        board = " {0} WON! ({1}-{2}) ".format(winner.name, self.player1.score, self.player2.score)
        score_text = scoreFont.render(board, True, pong.config.black, pong.config.white)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (800 // 2, 40)
        in_screen.blit(score_text, score_text_rect)


