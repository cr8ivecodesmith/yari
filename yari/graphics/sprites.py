"""
Sprites

"""

__all__ = ('Sprite', 'AnimatedSprite',)

from kivy.atlas import Atlas
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.graphics import (
    Rectangle as KivyRectangle,
    PushMatrix,
    PopMatrix,
)

from yari.graphics._properties import (
    PropPos, PropSize, PropFlip, PropTex, PropScale, PropRotate,
    PropVisible, PropDisable,
)
from yari.graphics.graphicsobject import GraphicsObject
from yari.types import Vector
from yari.utils import get_normal_tex_size


class Sprite(
    PropDisable, PropPos, PropSize, PropFlip, PropTex, PropScale, PropRotate,
    PropVisible, GraphicsObject
):
    """
    Basic Sprite

    """
    def __init__(self, source, pos=None, scale=None, **kwargs):
        super().__init__(**kwargs)

        scale = scale or 1.
        assert scale >= 0, 'Scale cannot be less than 0.'

        texture, size, orig_size = self._get_source_data(source, scale)

        self._scale = scale
        self._orig_size = orig_size
        self._source = source

        self._shape = KivyRectangle(texture=texture, pos=pos, size=size)
        self._update_origin()

        self.add(PushMatrix())
        self.add(self._rotation)
        self.add(self._shape)
        self.add(PopMatrix())

    def _get_source_data(self, source, scale):
        texture = Image(source).texture
        orig_size = get_normal_tex_size(texture)
        size = Vector(*orig_size) * scale
        return texture, size, orig_size

    @property
    def source(self): return self._source

    @source.setter
    def source(self, v):
        if self.disabled or self._source == v:
            return

        # Set new values
        texture, size, orig_size = self._get_source_data(v, self.scale)

        # Flip the image if needed
        iw, ih = size
        if getattr(self, 'flip_h', False):
            iw, _ = self._get_flip_h(iw, False, True, self.x)
        if getattr(self, 'flip_v', False):
            ih, _ = self._get_flip_v(ih, False, True, self.y)

        # Assign new values
        self._source = v
        self._orig_size = orig_size
        self.texture = texture
        self.size = (iw, ih)


class AnimatedSprite(
    PropDisable, PropPos, PropSize, PropFlip, PropTex, PropScale, PropRotate,
    PropVisible, GraphicsObject
):
    """
    Animated Sprite using Kivy Atlas

    The Atlas must follow a certain format.

    i.e. A Sprite Map with 2 animations: anim_a and anim_b
    Note that frame animations must be numbered after the name: `_1` to `_n`

    {
        'image.png': {
            'anim_a_1': [...],
            'anim_a_2': [...],
            'anim_b_1': [...],
            'anim_b_2': [...]
        }
    }

    """
    def __init__(
        self, source, animations, animation, speed=None, autoplay=False,
        pos=None, scale=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        assert animation in animations, 'Animation must be in Animations.'

        scale = scale or 1.
        assert scale >= 0, 'Scale cannot be less than 0.'

        # Initialize the sprite map
        self._source = source
        self._atlas = Atlas(source)

        # Initialize texture and size
        self.animations = animations
        self._animation = animation
        self._scale = scale
        self._orig_size = None

        # Initialize shape
        texture, size, orig_size = self._get_texture(animation, scale)
        self._orig_size = orig_size
        self._shape = KivyRectangle(texture=texture, pos=pos, size=size)
        self._update_origin()
        self.add(PushMatrix())
        self.add(self._rotation)
        self.add(self._shape)
        self.add(PopMatrix())

        # Animation control variables
        speed = speed or 5
        self._time = 0.
        self._speed = speed
        self._rate = 1. / speed
        self._frame = 1
        self._maxframes = len([
            k for k in self._atlas.textures.keys() if k.startswith(animation)
        ])
        self._clock = None

    def _get_texture(self, animation, scale, frame=None):
        frame = frame or 1
        texture = self._atlas[f'{animation}_{frame}']
        orig_size = get_normal_tex_size(texture)
        size = Vector(*orig_size) * scale
        return texture, size, orig_size

    def _handle_flip(self, size):
        iw, ih = size
        if getattr(self, 'flip_h', False):
            iw, _ = self._get_flip_h(iw, False, True, self.x)
        if getattr(self, 'flip_v', False):
            ih, _ = self._get_flip_v(ih, False, True, self.y)
        return iw, ih

    def _update_texture(self, animation, frame=None):
        texture, size, original_size = (
            self._get_texture(animation, self.scale, frame=frame)
        )
        self.size = self._handle_flip(size)
        self._orig_size = original_size
        self.texture = texture

    @property
    def source(self): return self._source

    @property
    def animation(self): return self._animation

    @animation.setter
    def animation(self, v):
        if self.disabled or self._animation == v:
            return
        self._animation = v
        self._frame = 1
        self._maxframes = len([
            k for k in self._atlas.textures.keys() if k.startswith(v)
        ])
        self._update_texture(v)

    @property
    def speed(self): return self._speed

    @speed.setter
    def speed(self, v):
        self._speed = v
        self._rate = 1. / v

    def play(self):
        if self._clock and self._clock.is_triggered:
            return
        if not self._clock:
            self._clock = Clock.schedule_interval(self._animate, 1./24)
        else:
            self._clock()

    def stop(self):
        if self._clock:
            self._clock.cancel()

    def _animate(self, delta):
        if self.disabled:
            return False

        self._time += delta
        if self._time > self._rate:
            self._time -= self._rate
            if self._frame >= self._maxframes:
                self._frame = 1
            else:
                self._frame += 1
            self._update_texture(self.animation, self._frame)
