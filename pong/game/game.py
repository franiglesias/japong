from game.game_mode import GameMode, TwoPlayers, OnePlayer
from game.side import Right, Left


class Game:
    game_mode: GameMode

    def __init__(self, side, game_mode):
        self.side_preference = side
        self.game_mode = game_mode

    def prefer_left(self):
        self.side_preference = Left()

    def prefer_right(self):
        self.side_preference = Right()

    def prefer_two_players(self):
        self.game_mode = TwoPlayers()

    def prefer_one_player(self):
        self.game_mode = OnePlayer()
