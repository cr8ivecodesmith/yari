"""
Background Color Mixin

NOTE:

- Whenever possible, this should be the first inherited component.

"""
__all__ = ('BackgroundColor',)

from functools import partial

from kivy.graphics import Rectangle, Color
from kivy.properties import ListProperty

from yari.utils import property_setter


class BackgroundColor:

    background_color = ListProperty([1, 1, 1, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self._inst_bg_color = Color(rgba=self.background_color)
            self._inst_bg_color_rect = Rectangle(
                size=self.size, pos=self.pos
            )

        self.bind(
            size=partial(
                property_setter,
                other=self._inst_bg_color_rect, other_prop='size'
            ),
            pos=partial(
                property_setter,
                other=self._inst_bg_color_rect, other_prop='pos'
            ),
            background_color=partial(
                property_setter,
                other=self._inst_bg_color, other_prop='rgba'
            ),
        )
