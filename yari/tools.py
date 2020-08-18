"""
Collection of Node tools

"""

__all__ = ('RuntimeStats',)

from kivy.clock import Clock

from kivy.properties import NumericProperty, BooleanProperty

from yari.ui import Label
from yari.core import Node


class RuntimeStats(Node):
    """
    Runtime Stats System

    TODO:

    - When reset position on Node tree to topmost whenever show is set to True
    - Make a show / hide method
    - Show delta of last frame time
    - Refactor. I don't we need to use Kivy Properties for these stats.
    - Set schduled_interval delay to 0

    """

    boottime = NumericProperty()
    fps = NumericProperty()
    rfps = NumericProperty()
    frames_drawn = NumericProperty()
    frames_total = NumericProperty()
    last_frame_time = NumericProperty()

    show = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label = Label(
            pos=(30, 5), font_size='12sp',
            color=(1, 1, 1, 1),
        )
        label.hide()
        self.label = label

        self.bind(
            fps=self.update_text,
            rfps=self.update_text,
            boottime=self.update_text,
            frames_drawn=self.update_text,
            frames_total=self.update_text,
            last_frame_time=self.update_text,
            show=self.do_show,
        )

        self.add_widget(label)

        self._clock = Clock.schedule_interval(self.update, 1.0)
        self._clock.cancel()

    def do_show(self, this, value):
        if value:
            self.label.show()
            self._clock()
        else:
            self.label.hide()
            self._clock.cancel()

    def update_text(self, instance, value):
        fd = self.frames_drawn
        ft = self.frames_total
        fx = ft - fd
        text = (
            f'FPS: {self.rfps} (ave: {self.fps:.1f})\n'
            f'FRAMES: {fd} of {ft} ({fx})\n'
            f'TIME SPENT LAST FRAME: {self.last_frame_time}\n'
            f'RUNTIME: {self.boottime:.2f}s'
        )
        self.label.text = text

    def update(self, dt):
        self.boottime = Clock.get_boottime()
        self.fps = Clock.get_fps()
        self.rfps = Clock.get_rfps()
        self.frames_drawn = Clock.frames_displayed
        self.frames_total = Clock.frames
        self.last_frame_time = Clock.frametime
