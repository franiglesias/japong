from config import styles
from utils.line import Line


class ScoreBoard:
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def draw(self, scene):
        lines = [
            Line(self.points(), styles['score']),
            Line(self.sets(), styles['sets'])
        ]
        scene.text_writer.blits(lines, ('center', 30))

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

        line = Line("{0} WON".format(winner.name), styles['end_title'])

        scene.text_writer.blits([line], ('center', 'top'))

        partials = self.score_manager.partials()

        lines = [Line(self.sets(), styles['score'])]
        for set_index in range(len(partials[0])):
            line = "{0} - {1}".format(
                partials[0][set_index],
                partials[1][set_index]
            )
            lines.append(Line(line, styles['sets']))

        scene.text_writer.blits(lines, ('center', 'middle'))
