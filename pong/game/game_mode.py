from config import computer_speed, left_keys, human_speed, right_keys
from field.reacts_to_ball import ReactsToBall
from game.control.computer_control_engine import ComputerControlEngine
from game.control.keyboard_control_engine import KeyboardControlEngine
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

    def player_one(self):
        return Player(
            'computer',
            Left(),
            KeyboardControlEngine(self.ball),
            computer_speed
        )

    def player_two(self):
        return Player(
            'computer',
            Right(),
            ComputerControlEngine(self.ball),
            computer_speed
        )

    def str(self):
        return 'comp/comp'


class OnePlayer(GameMode):
    def player_one(self):
        return Player(
            'human',
            Left(),
            KeyboardControlEngine(left_keys),
            human_speed
        )

    def player_two(self):
        return Player(
            'computer',
            Right(),
            ComputerControlEngine(self.ball),
            computer_speed
        )

    def str(self):
        return '1 player'


class TwoPlayers(GameMode):
    def player_one(self):
        return Player(
            'human',
            Left(),
            KeyboardControlEngine(left_keys),
            human_speed
        )

    def player_two(self):
        return Player(
            'other',
            Right(),
            KeyboardControlEngine(right_keys),
            human_speed
        )

    def str(self):
        return 'Two players'
