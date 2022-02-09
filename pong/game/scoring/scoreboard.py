from config import styles
from utils.line import Line


class ScoreBoard:
    """Displays the results from score_manager data"""
    def __init__(self, score_manager):
        self.score_manager = score_manager

    def draw(self, scene):
        """Updates results during game"""
        lines = [
            Line(f'{self.points(0)}   {self.points(1)}', styles['score']),
            Line(f'{self.sets(0)}   {self.sets(1)}', styles['sets'])
        ]
        scene.text_writer.blits(lines, ('center', 30))

    def points(self, side):
        """Points won by player"""
        return self.score_manager.points()[side]

    def sets(self, left):
        """Sets won by player"""
        return self.score_manager.sets()[left]

    def final_board(self, scene):
        """Shows final board with detailed data"""
        winner = self.score_manager.winner()

        line = Line(f"{winner.name} WON", styles['end_title'])

        scene.text_writer.blits([line], ('center', 'top'))

        partials = self.score_manager.partials()

        lines = [Line(f'{self.sets(0)}   {self.sets(1)}', styles['score'])]
        for set_index in range(len(partials[0])):
            line = f"{partials[0][set_index]} - {partials[1][set_index]}"
            lines.append(Line(line, styles['sets']))

        scene.text_writer.blits(lines, ('center', 'middle'))
