import sys

from app.app import App
# Init game engine
from config import POINTS_TO_WIN, SETS_TO_WIN, MINIMUM_DIFF
from game.scoring.match import Match

if __name__ == '__main__':
    app = App(Match(SETS_TO_WIN, POINTS_TO_WIN, MINIMUM_DIFF))
    code = app.run()
    sys.exit(code)
