from config import human_side
from config import human_speed
from config import game_mode
from config import computer_speed


class Game(object):

    def __init__(self):
        self.side_preference = human_side
        self.game_mode = game_mode
        self.computer_speed = computer_speed
        self.human_speed = human_speed

    def set_side_preference(self, side_preference):
        self.side_preference = side_preference

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode
