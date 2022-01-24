from unittest import TestCase

from game.pad import Pad
from game.side import Left
from pong.game.control.keyboard_control_engine import KeyboardControlEngine
from tests.events import r_key_event, u_key_event, d_key_event


class TestKeyboardControlEngine(TestCase):

    def setUp(self) -> None:
        self.engine = KeyboardControlEngine(('u', 'd'))
        self.pad = Pad(Left(), self.engine)
        self.pad.rect.y = 100

    def test_should_ignore_some_keys(self):
        self.engine.handle([r_key_event])

        self.assertEqual(0, self.pad.dy)

    def test_press_up_key_should_move_pad_up(self):
        self.engine.handle([u_key_event])

        self.assertEqual(-2, self.pad.dy)

    def test_press_down_key_should_move_pad_down(self):
        self.engine.handle([d_key_event])

        self.assertEqual(2, self.pad.dy)
