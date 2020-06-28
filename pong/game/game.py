import pong.config


class Game(object):

    def __init__(self):
        self.side_preference = pong.config.human_side

    def set_side_preference(self, side_preference):
        self.side_preference = side_preference
