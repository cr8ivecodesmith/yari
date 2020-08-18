__all__ = ('Label', 'KvLabel',)

from kivy.uix.label import Label as KivyLabel

from yari.core import Node
from yari.mixins import (
    BackgroundColor,
    Rotation,
    Visibility,
)


class Label(Node, BackgroundColor, Rotation, Visibility, KivyLabel):
    pass


class KvLabel(Label): pass  # noqa
