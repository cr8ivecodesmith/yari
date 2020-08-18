__all__ = ('FloatLayout', 'KvFloatLayout')

from kivy.uix.floatlayout import FloatLayout as KivyFloatLayout

from yari.core import Node
from yari.mixins import BackgroundColor


class FloatLayout(Node, BackgroundColor, KivyFloatLayout):
    pass


class KvFloatLayout(FloatLayout): pass  # noqa
