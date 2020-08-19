__all__ = ('Text',)

from kivy.core.text import Label as KivyCoreLabel, DEFAULT_FONT
from kivy.graphics import (
    Color as KivyColor,
    Rectangle as KivyRectangle,
    PushMatrix,
    PopMatrix,
)

from yari.graphics._properties import (
    PropPos, PropSize, PropColor, PropDisable, PropVisible, PropRotate,
)
from yari.graphics.colors import OFFWHITE
from yari.graphics.graphicsobject import GraphicsObject
from yari.utils import get_normal_tex_size


class Text(
    PropDisable, PropVisible, PropColor, PropPos, PropSize,
    PropRotate, GraphicsObject
):
    """
    Text

    A direct text drawing on the canvas without having to create it's own
    widget.

    This is not as feature complete as kivy.uix.label. If you need more
    functionality in your text, use that instead.

    TODO: Allow updating other supported text properties.

    """

    # Full set of kivy.core.text properties.
    # NOTE: Not all are implemented.
    _font_properties = ('text', 'font_size', 'font_name', 'bold', 'italic',
                        'underline', 'strikethrough', 'font_family', 'color',
                        'disabled_color', 'halign', 'valign', 'padding_x',
                        'padding_y', 'outline_width', 'disabled_outline_color',
                        'outline_color', 'text_size', 'shorten', 'mipmap',
                        'line_height', 'max_lines', 'strip', 'shorten_from',
                        'split_str', 'ellipsis_options', 'unicode_errors',
                        'markup', 'font_hinting', 'font_kerning',
                        'font_blended', 'font_context', 'font_features',
                        'base_direction', 'text_language')

    def __init__(
        self, text, font_size=12, font_name=DEFAULT_FONT,
        bold=False, italic=False, underline=False, strikethrough=False,
        halign='left', valign='bottom', line_height=1.,
        pos=None, color=None, alpha=1.,
        **kwargs
    ):
        super().__init__(**kwargs)
        self._is_pos_int = True

        # Initialize text object
        self._ktext = None
        self._update_ktext(
            text=text, font_size=font_size,
            font_name=font_name,
            bold=bold, italic=italic, underline=underline,
            strikethrough=strikethrough,
            halign=halign, valign=valign, line_height=line_height,
        )
        texture = self._ktext.texture
        size = get_normal_tex_size(texture)

        self._color = KivyColor(rgb=color or OFFWHITE, a=alpha)
        self._shape = KivyRectangle(
            texture=texture, size=size, pos=pos
        )
        self._update_origin()

        self.add(PushMatrix())
        self.add(self._rotation)
        self.add(self._color)
        self.add(self._shape)
        self.add(PopMatrix())

    def _update_ktext(self, **kwargs):
        keys = set(kwargs.keys()) & set(self._font_properties)
        params = {k: kwargs[k] for k in keys}
        self._ktext = KivyCoreLabel(**params)
        self._ktext.refresh()

    def _update_shape_tex(self):
        self._ktext.refresh()
        self._shape.texture = self._ktext.texture

    def reset_norm_size(self):
        """Resets text size to font size

        """
        self.size = get_normal_tex_size(self._ktext.texture)

    @property
    def text(self): return self._ktext.text

    @text.setter
    def text(self, v):
        if getattr(self, 'disabled', False):
            return
        self._ktext.text = v
        self._update_shape_tex()
        self.reset_norm_size()
