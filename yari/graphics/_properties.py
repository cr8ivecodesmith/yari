"""
Property Setters and Getters

Common GraphicsObject properties for convenience.

Setters must check the disabled property before allowing the value
to be updated.

"""

__all__ = (
    'PropPos', 'PropSize', 'PropPoints', 'PropColor', 'PropFlip',
    'PropTex', 'PropScale', 'PropRotate', 'PropVisible',
    'PropDisable',
)

from kivy.graphics import Rotate

from yari.types import Vector


class PropDisable:

    disabled = False


class PropPos:

    def __init__(self, **kwargs):
        self._is_pos_int = False
        super().__init__(**kwargs)

    @property
    def x(self): return self._shape.pos[0]

    @x.setter
    def x(self, v):
        if getattr(self, 'disabled', False):
            return
        v = v if not self._is_pos_int else round(v)
        self.pos = (v, self._shape.pos[1])

    @property
    def y(self): return self._shape.pos[1]

    @y.setter
    def y(self, v):
        if getattr(self, 'disabled', False):
            return
        v = v if not self._is_pos_int else round(v)
        self.pos = (self._shape.pos[0], v)

    @property
    def pos(self): return self._shape.pos

    @pos.setter
    def pos(self, v):
        if getattr(self, 'disabled', False):
            return

        v = v if not self._is_pos_int else (round(v[0]), round(v[1]))
        self._shape.pos = v

        # Update rotation origin if needed.
        update_origin = getattr(self, '_update_origin', None)
        if update_origin:
            update_origin()


class PropSize:

    @property
    def width(self): return self._shape.size[0]

    @width.setter
    def width(self, v):
        if getattr(self, 'disabled', False):
            return
        self.size = (v, self._shape.size[1])

    @property
    def height(self): return self._shape.size[1]

    @height.setter
    def height(self, v):
        if getattr(self, 'disabled', False):
            return
        self.size = (self._shape.size[0], v)

    @property
    def size(self): return self._shape.size

    @size.setter
    def size(self, v):
        if getattr(self, 'disabled', False):
            return

        self._shape.size = v

        # Update rotation origin if needed.
        update_origin = getattr(self, '_update_origin', None)
        if update_origin:
            update_origin()


class PropPoints:

    @property
    def points(self): return self._shape.points

    @points.setter
    def points(self, v):
        if getattr(self, 'disabled', False):
            return
        self._shape.points = v


class PropColor:

    @property
    def color(self): return self._color.rgb

    @color.setter
    def color(self, v):
        if getattr(self, 'disabled', False):
            return
        self._color.rgb = v

    @property
    def alpha(self): return self._color.a

    @alpha.setter
    def alpha(self, v):
        if getattr(self, 'disabled', False):
            return
        if 0. <= v <= 1.:
            self._color.a = v


class PropFlip:
    """Flips the image horizontally or vertically
    by setting the width or height to a negative value.

    Requires: PropSize, PropPos

    If using on objects with textures (i.e. Sprites) that manipulates
    scale and source, make sure that it also accounts if the image was
    previously flipped.

    """

    def __init__(self, **kwargs):
        self._flip_h = False
        self._flip_v = False
        super().__init__(**kwargs)

    def _get_flip_h(self, width, prev_v, v, x):
        w = abs(width)
        if not prev_v and v:
            x += w
        elif prev_v and not v:
            x -= w
        w *= -1 if v else 1
        return w, x

    def _get_flip_v(self, height, prev_v, v, y):
        h = abs(height)
        if not prev_v and v:
            y += h
        elif prev_v and not v:
            y -= h
        h *= -1 if v else 1
        return h, y

    @property
    def flip_h(self): return self._flip_h

    @flip_h.setter
    def flip_h(self, v):
        if getattr(self, 'disabled', False):
            return
        w, x = self._get_flip_h(self.width, self._flip_h, v, self.x)
        self.width = w
        self.x = x
        self._flip_h = v

    @property
    def flip_v(self): return self._flip_v

    @flip_v.setter
    def flip_v(self, v):
        if getattr(self, 'disabled', False):
            return
        h, y = self._get_flip_v(self.height, self._flip_v, v, self.y)
        self.height = h
        self.y = y
        self._flip_v = v


class PropTex:

    @property
    def texture(self): return self._shape.texture

    @texture.setter
    def texture(self, v):
        if getattr(self, 'disabled', False):
            return
        self._shape.texture = v


class PropScale:
    """
    Scale Property

    Requires: PropSize, PropPos

    Optional handling: PropFlip

    """
    def __init__(self, scale=None, **kwargs):
        self._scale = scale or 1.
        self._orig_size = (100, 100)
        super().__init__(**kwargs)

    @property
    def scale(self): return self._scale

    @scale.setter
    def scale(self, v):
        if getattr(self, 'disabled', False):
            return

        if v < 0:
            v = 0

        # Calc new values
        new_size = Vector(*self._orig_size) * v
        diff = (self.size - new_size) / 2
        new_pos = self.pos + diff

        # Flip the image if needed
        iw, ih = new_size
        ix, iy = new_pos
        if getattr(self, 'flip_h', False):
            iw, ix = self._get_flip_h(iw, False, True, ix)
        if getattr(self, 'flip_v', False):
            ih, iy = self._get_flip_v(ih, False, True, iy)

        # Assign new values
        self._scale = v
        self.size = (iw, ih)
        self.pos = (ix, iy)


class PropRotate:
    """
    Rotation Property

    When using this property, you will have to compose the graphics object(s)
    between a PushMatrix and PopMatrix instruction.

    i.e.

    PushMatrix()
    Rotate()
    GraphicsObject()
    PopMatrix()

    Furthermore, the rotation origin is always relative to the position and
    size so the PropPos and PropSize call on the `_update_origin` method
    whenever they are updated.

    Requires: PropSize, PropPos
    Updated by: PropSize, PropPos

    """
    def __init__(self, **kwargs):
        self._rotation = Rotate()
        super().__init__(**kwargs)

    def _update_origin(self):
        w, h = self.size
        x, y = self.pos
        cx, cy = x + w / 2, y + h / 2
        self.origin = (cx, cy)

    @property
    def angle(self): return self._rotation.angle

    @angle.setter
    def angle(self, v):
        if getattr(self, 'disabled', False):
            return

        if v > 359.9 or v < -359.9:
            v = 0.
        self._rotation.angle = v

    @property
    def origin(self): return self._rotation.origin

    @origin.setter
    def origin(self, v):
        if getattr(self, 'disabled', False):
            return
        self._rotation.origin = v

    @property
    def axis(self): return self._rotation.axis

    @axis.setter
    def axis(self, v):
        if getattr(self, 'disabled', False):
            return
        self._rotation.axis = v


class PropVisible:
    """
    Visibility Property

    This sets the object's size to 0 and disables it.

    Requires: PropDisable, PropSize

    """

    def __init__(self, **kwargs):
        self._visible = True
        self._visible_size = None
        self._hidden_size = (0, 0)
        super().__init__(**kwargs)

    @property
    def visible(self): return self._visible

    @visible.setter
    def visible(self, v):
        if v and not self._visible:
            self.show()
        elif not v and self._visible:
            self.hide()

    def show(self):
        if self._visible or self._visible_size is None:
            return
        self.disabled = False
        self.size = self._visible_size
        self._visible = True

    def hide(self):
        if not self._visible:
            return
        self._visible_size = self.size
        self.size = self._hidden_size
        self._visible = False
        self.disabled = True
