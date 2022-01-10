from config import computer_speed
from config import game_mode
from config import human_side, left_keys, right_keys
from config import human_speed
from field.reacts_to_ball import ReactsToBall
from game.control.computer_control_engine import ComputerControlEngine
from game.control.keyboard_control_engine import KeyboardControlEngine
from game.player import Player
from game.side import Side, Right, Left


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
            'human',
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
            human_speed
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
