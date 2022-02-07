from config import styles


class ScoreBoard:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def draw(self, scene):
        lines = [
            (self.points(), styles['score']),
            (self.sets(), styles['sets'])
        ]
        scene.text_writer.multi_blit(lines, ('center', 40))

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

        line = ("{0} WON".format(winner.name), styles['end_title'])

        scene.text_writer.multi_blit([line], ('center', 30))

        partials = self.score_manager.partials()

        lines = [(self.sets(), styles['score'])]
        for set_index in range(len(partials[0])):
            line = "{0} - {1}".format(
                partials[0][set_index],
                partials[1][set_index]
            )
            lines.append((line, styles['sets']))

        scene.text_writer.multi_blit(lines, ('center', 160))
