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

    def prefer_right(self):
        self.side_preference = 'right'

    def prefer_left(self):
        self.side_preference = 'left'

    def prefer_two_players(self):
        self.game_mode = 2

    def prefer_one_player(self):
        self.game_mode = 1
