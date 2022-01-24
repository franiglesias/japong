from unittest import TestCase

from pygame.event import Event

import pong.config
import pong.tests.events
from game.ball import Ball
from game.control.computer_control_engine import ComputerControlEngine
from game.pad import Pad
from game.side import Left


class TestComputerControlEngine(TestCase):

    def setUp(self) -> None:
        self.ball = Ball(pong.config.white, 10)
        self.engine = ComputerControlEngine(self.ball)
        self.pad = Pad(Left(), 1, self.engine)
        self.pad.rect.y = 100

    def test_invalid_event_does_not_move_pad(self):
        self.ball.rect.y = 200

        self.engine.handle([pong.tests.events.any_key_event])
        self.assertEqual(0, self.pad.dy)

    def test_valid_event_does_not_move_pad(self):
        self.ball.rect.y = 200
        event_move = Event(pong.config.COMPUTER_MOVES_EVENT)
        self.engine.handle([event_move])
        self.assertEqual(1, self.pad.dy)

    def test_mixed_events_are_handled_or_not(self):
        self.ball.rect.y = 200
        events = [
            Event(pong.config.COMPUTER_MOVES_EVENT),
            pong.tests.events.any_key_event
        ]
        self.engine.handle(events)
        self.assertEqual(1, self.pad.dy)
