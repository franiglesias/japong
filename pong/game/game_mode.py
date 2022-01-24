from config import computer_speed, left_keys, human_speed, right_keys
from field.reacts_to_ball import ReactsToBall
from game.control.computer_control_engine import ComputerControlEngine
from game.control.keyboard_control_engine import KeyboardControlEngine
from game.pad import Pad
from game.player import Player
from game.side import Left, Right


class GameMode(ReactsToBall):

    def __init__(self):
        pass

    @staticmethod
    def from_raw(raw_game_mode):
        if raw_game_mode == 1:
            return OnePlayer()
        if raw_game_mode == 2:
            return TwoPlayers()

    def equals(self, other):
        return type(self) == type(other)

    def player_one(self):
        pad = Pad(Left(), computer_speed, ComputerControlEngine(self.ball))
        return Player('computer', Left(), pad)

    def player_two(self):
        pad = Pad(Right(), computer_speed, ComputerControlEngine(self.ball))
        return Player('computer', Right(), pad)

    def str(self):
        return 'comp/comp'


class OnePlayer(GameMode):
    def player_one(self):
        pad = Pad(Left(), human_speed, KeyboardControlEngine(left_keys))

        return Player('human', Left(), pad)

    def player_two(self):
        pad = Pad(Right(), computer_speed, ComputerControlEngine(self.ball))
        return Player('computer', Right(), pad)

    def str(self):
        return '1 player'


class TwoPlayers(GameMode):
    def player_one(self):
        pad = Pad(Left(), human_speed, KeyboardControlEngine(left_keys))

        return Player('human', Left(), pad)

    def player_two(self):
        pad = Pad(Right(), human_speed, KeyboardControlEngine(right_keys))

        return Player('other', Right(), pad)

    def str(self):
        return 'Two players'
