import sys

from app.app import App
from game.scoring.match import Match
from utils.configuration import read_configuration


def main():
    """
    Inits the game loop
    """
    match = read_configuration('match')
    app = App(Match(
        match.getint('sets_to_win'),
        match.getint('points_to_win'),
        match.getint('minimum_diff')
    ))
    code = app.run()
    sys.exit(code)


if __name__ == '__main__':
    main()
