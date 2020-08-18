"""
Sound System

"""

__all__ = ('Sound',)

from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, BooleanProperty

from yari.core import Node


class Sound(Node):

    source = StringProperty()
    autoplay = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_event('on_play')
        self.create_event('on_stop')

        self._audio = None
        self._is_playing = False
        self.bind(autoplay=self.play)

    def play(self, *args):
        if not self._audio:
            self._audio = SoundLoader.load(self.source)
        if not self._audio.state == 'playing':
            self._audio.play()
            self.broadcast('on_play')

    def stop(self, *args):
        if self._audio:
            self._audio.stop()
            self.broadcast('on_stop')
