from unittest import TestCase

from pygame.event import Event

from config import white, COMPUTER_MOVES_EVENT
from game.ball import Ball
from game.control.computer_control_engine import ComputerControlEngine
from game.pad import Pad
from game.side import Left
from tests.events import any_key_event


class TestComputerControlEngine(TestCase):

    def setUp(self) -> None:
        self.ball = Ball(white, 10)
        self.engine = ComputerControlEngine(self.ball)
        self.pad = Pad(Left(), self.engine)
        self.pad.rect.y = 100

    def test_invalid_event_does_not_move_pad(self):
        self.ball.rect.y = 200

        self.engine.handle([any_key_event])
        self.assertEqual(0, self.pad.dy)

    def test_valid_event_does_not_move_pad(self):
        self.ball.rect.y = 200
        event_move = Event(COMPUTER_MOVES_EVENT)
        self.engine.handle([event_move])
        self.assertEqual(1, self.pad.dy)

    def test_mixed_events_are_handled_or_not(self):
        self.ball.rect.y = 200
        events = [
            Event(COMPUTER_MOVES_EVENT),
            any_key_event
        ]
        self.engine.handle(events)
        self.assertEqual(1, self.pad.dy)
