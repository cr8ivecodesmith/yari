"""
Shapes

These shapes have to be added to a canvas instance.

TODO:

Base:

- Bezier
- Poly (Mesh?)
- RoundedRectangle

Outline versions: all base shapes with *Line

- Fix implementation of shapes without a natural `pos` property.

"""

__all__ = ('Rectangle', 'Ellipse', 'Point', 'Line', 'Triangle',)

from kivy.graphics import (
    Color as KivyColor,
    Point as KivyPoint,
    Rectangle as KivyRectangle,
    Ellipse as KivyEllipse,
    Line as KivyLine,
    Triangle as KivyTriangle,
)

from yari.graphics._properties import (
    PropPos, PropSize, PropPoints, PropColor,
)
from yari.graphics.colors import OFFWHITE
from yari.graphics.graphicsobject import GraphicsObject


class Point(PropColor, PropPoints, GraphicsObject):

    def __init__(
        self, points=None, pointsize=1.,
        color=None, alpha=1.,
        **kwargs
    ):
        super().__init__(**kwargs)

        self._color = KivyColor(rgb=color or OFFWHITE, a=alpha)
        self._shape = KivyPoint(
            points=points, pointsize=pointsize,
        )

        self.add(self._color)
        self.add(self._shape)

    @property
    def pointsize(self): return self._shape.pointsize

    @pointsize.setter
    def pointsize(self, v): self._shape.pointsize = v


class Line(PropColor, PropPoints, GraphicsObject):
    """A Line shape

    TODO:
    - Apply other line parameters from: https://github.com/kivy/kivy/blob/master/kivy/graphics/vertex_instructions_line.pxi#L33

    """  # noqa

    def __init__(
        self, points=None, width=1.,
        color=None, alpha=1.,
        **kwargs
    ):
        super().__init__(**kwargs)

        self._color = KivyColor(rgb=color or OFFWHITE, a=alpha)
        self._shape = KivyLine(
            points=points, width=width,
        )

        self.add(self._color)
        self.add(self._shape)

    @property
    def width(self): return self._shape.width

    @width.setter
    def width(self, v): self._shape.width = v


class Rectangle(PropColor, PropPos, PropSize, GraphicsObject):

    def __init__(self, pos=None, size=None, color=None, alpha=1., **kwargs):
        super().__init__(**kwargs)

        self._color = KivyColor(rgb=color or OFFWHITE, a=alpha)
        self._shape = KivyRectangle(pos=pos, size=size)

        self.add(self._color)
        self.add(self._shape)


class Ellipse(Rectangle):

    def __init__(
        self, pos=None, size=None,
        segments=180, angle_start=0., angle_end=360.,
        color=None, alpha=1.,
        **kwargs
    ):
        super().__init__(**kwargs)

        self._color = KivyColor(rgb=color or OFFWHITE, a=alpha)
        self._shape = KivyEllipse(
            pos=pos, size=size,
            segments=segments, angle_start=angle_start, angle_end=angle_end,
        )

        self.add(self._color)
        self.add(self._shape)

    @property
    def segments(self): return self._shape.segments

    @segments.setter
    def segments(self, v): self._shape.segments = v

    @property
    def angle_start(self): return self._shape.angle_start

    @angle_start.setter
    def angle_start(self, v): self._shape.angle_start = v

    @property
    def angle_end(self): return self._shape.angle_end

    @angle_end.setter
    def angle_end(self, v): self._shape.angle_end = v


class Triangle(PropColor, PropPoints, GraphicsObject):

    def __init__(self, points=None, color=None, alpha=1., **kwargs):
        super().__init__(**kwargs)

        self._color = KivyColor(rgb=color or OFFWHITE, a=alpha)
        self._shape = KivyTriangle(points=points)

        self.add(self._color)
        self.add(self._shape)
