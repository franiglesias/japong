from unittest import TestCase

import pong
import pong.game.control.keyboard_control_engine
import pong.game.pad
import pong.tests.events
from game.side import Left


class TestKeyboardControlEngine(TestCase):

    def setUp(self) -> None:
        self.engine = pong.game.control.keyboard_control_engine.KeyboardControlEngine(('u', 'd'))
        self.pad = pong.game.pad.Pad(Left(), 1, self.engine)
        self.pad.rect.y = 100

    def test_should_ignore_some_keys(self):
        self.engine.handle([pong.tests.events.r_key_event])

        self.assertEqual(0, self.pad.dy)

    def test_press_up_key_should_move_pad_up(self):
        up_key_event = pong.tests.events.u_key_event
        self.engine.handle([up_key_event])

        self.assertEqual(-1, self.pad.dy)

    def test_press_down_key_should_move_pad_down(self):
        down_key_event = pong.tests.events.d_key_event
        self.engine.handle([down_key_event])

        self.assertEqual(1, self.pad.dy)
