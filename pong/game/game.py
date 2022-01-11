from config import game_mode
from config import human_side
from game.game_mode import GameMode, TwoPlayers, OnePlayer
from game.side import Side, Right, Left


class Game(object):
    game_mode: GameMode

    def __init__(self):
        self.side_preference = Side.from_raw(human_side)
        self.game_mode = GameMode.from_raw(game_mode)

    def prefer_right(self):
        self.side_preference = Right()

    def prefer_left(self):
        self.side_preference = Left()

    def prefer_two_players(self):
        self.game_mode = TwoPlayers()

    def prefer_one_player(self):
        self.game_mode = OnePlayer()

    def player_one(self):
        return self.game_mode.player_one()

    def player_two(self):
        return self.game_mode.player_two()
