import configparser
import sys

from app.app import App
from game.scoring.match import Match


def main():
    """
    Inits the game loop
    """
    match = read_match_configuration()
    app = App(Match(
        match.getint('sets_to_win'),
        match.getint('points_to_win'),
        match.getint('minimum_diff')
    ))
    code = app.run()
    sys.exit(code)


def read_match_configuration():
    """
    Reads the configuration data for match
    """
    cfg = configparser.ConfigParser()
    cfg.read('./config.toml')
    match = cfg['match']
    return match


if __name__ == '__main__':
    main()
