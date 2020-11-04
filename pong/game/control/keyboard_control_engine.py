from pygame import key, KEYDOWN, KEYUP

from pong.game.control.control_engine import ControlEngine


class KeyboardControlEngine(ControlEngine):
    def __init__(self, keys):
        super().__init__()
        self.upKey = keys[0]
        self.downKey = keys[1]

    def handle(self, events):
        for event in events:
            if event.type == KEYUP:
                key_name = key.name(event.key)
                if key_name == self.upKey or key_name == self.downKey:
                    self.pad.stop()
            elif event.type == KEYDOWN:
                key_name = key.name(event.key)
                if key_name == self.upKey:
                    self.pad.up()
                elif key_name == self.downKey:
                    self.pad.down()

