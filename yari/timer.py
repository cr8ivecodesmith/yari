"""
Timer System

"""

__all__ = ('Timer',)

from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    BoundedNumericProperty,
)

from yari.core import Node


class Timer(Node):

    delay = BoundedNumericProperty(1, min=0., max=3600.)  # seconds
    oneshot = BooleanProperty(False)
    autostart = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_event('on_timeout')
        self.bind(
            oneshot=self.handle_oneshot,
            autostart=self.start,
            delay=self.handle_delay,
        )

        self._clock = None
        self._scheduler = Clock.schedule_interval
        self.delta = 0.

    def handle_oneshot(self, this, value):
        if self._clock and self._clock.is_triggered:
            self._clock.stop()
        self._scheduler = getattr(
            Clock, 'schedule_once' if value else 'schedule_interval'
        )

    def handle_delay(self, this, value):
        self.stop()
        self._clock = None
        self.start()

    def start(self, *args):
        if self._clock and self._clock.is_triggered:
            return
        if not self._clock:
            print(f'Clock starting with delay: {self.delay}')
            self._clock = self._scheduler(self._tick, self.delay)
        else:
            self._clock()

    def stop(self):
        if self._clock:
            self._clock.cancel()

    def _tick(self, dt):
        self.delta = dt
        self.broadcast('on_timeout', dt)
