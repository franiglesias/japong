from pong.config import style_score, style_sets, style_end_title


class ScoreBoard:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def draw(self, scene):
        lines = [
            (self.points(), style_score),
            (self.sets(), style_sets)
        ]
        scene.text_renderer.multi_blit(lines, ('center', 40))

    def points(self):
        return "{0}   {1}".format(
            self.score_manager.points()[0],
            self.score_manager.points()[1],
        )

    def sets(self):
        return "{0}   {1}".format(
            self.score_manager.sets()[0],
            self.score_manager.sets()[1],
        )

    def end_of_game(self):
        return self.score_manager.end_of_game()

    def final_board(self, scene):
        winner = self.score_manager.winner()

        line = (
            "{0} WON".format(winner.name), style_end_title
        )

        scene.text_renderer.multi_blit([line], ('center', 30))

        partials = self.score_manager.partials()

        lines = [(self.sets(), style_score)]
        for set_index in range(len(partials[0])):
            line = "{0} - {1}".format(
                partials[0][set_index],
                partials[1][set_index]
            )
            lines.append((line, style_sets))

        scene.text_renderer.multi_blit(lines, ('center', 160))
