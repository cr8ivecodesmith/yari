"""
Rotation Mixin

TODO:

- Allow setting of rotation origin and axis

"""
__all__ = ('Rotation',)

from functools import partial

from kivy.graphics import PushMatrix, Rotate, PopMatrix
from kivy.properties import NumericProperty

from yari.utils import property_setter


class Rotation:

    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            PushMatrix()
            self._inst_rotate = Rotate(
                angle=self.angle,
                origin=self.center,
                axis=(0, 0, 1)
            )

        with self.canvas.after:
            PopMatrix()

        self.bind(
            angle=partial(
                property_setter,
                other=self._inst_rotate, other_prop='angle'
            ),
            center=partial(
                property_setter,
                other=self._inst_rotate, other_prop='origin'
            ),
        )
