import pong.config


class Game(object):

    def __init__(self):
        self.side_preference = pong.config.human_side
        self.game_mode = pong.config.game_mode
        self.computer_speed = pong.config.computer_speed
        self.human_speed = pong.config.human_speed

    def set_side_preference(self, side_preference):
        self.side_preference = side_preference

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode
