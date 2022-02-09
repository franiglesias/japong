from config import LEFT_KEYS, RIGHT_KEYS
from field.bound_to_ball import BoundToBall
from game.control.computer_control_engine import ComputerControlEngine
from game.control.keyboard_control_engine import KeyboardControlEngine
from game.pad import Pad
from game.player import Player
from game.side import Left, Right


class GameMode(BoundToBall):

    def __init__(self):
        pass

    @staticmethod
    def from_raw(raw_game_mode):
        modes = [
            OnePlayer(),
            TwoPlayers()
        ]
        return modes[int(raw_game_mode) - 1]

    def equals(self, other):
        return type(self) == type(other)

    def player_one(self):
        pad = Pad(Left(), ComputerControlEngine(self.ball))
        player = Player('computer', Left())

        return pad, player

    def player_two(self):
        pad = Pad(Right(), ComputerControlEngine(self.ball))
        player = Player('computer', Right())

        return pad, player

    def str(self):
        return 'comp/comp'


class OnePlayer(GameMode):
    def player_one(self):
        pad = Pad(Left(), KeyboardControlEngine(LEFT_KEYS))
        player = Player('human', Left())

        return pad, player

    def player_two(self):
        pad = Pad(Right(), ComputerControlEngine(self.ball))
        player = Player('computer', Right())

        return pad, player

    def str(self):
        return '1 player'


class TwoPlayers(GameMode):
    def player_one(self):
        pad = Pad(Left(), KeyboardControlEngine(LEFT_KEYS))
        player = Player('human', Left())

        return pad, player

    def player_two(self):
        pad = Pad(Right(), KeyboardControlEngine(RIGHT_KEYS))
        player = Player('other', Right())

        return pad, player

    def str(self):
        return 'Two players'
