"""
Visibility Mixin

"""
__all__ = ('Visibility',)

from kivy.properties import BooleanProperty


def handle_visibility(this, value):
    this.size_hint_x = 1 if this.visible else 0
    this.opacity = 1 if this.visible else 0
    this.disabled = not this.visible


class Visibility:

    visible = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bind(visible=handle_visibility)

    def hide(self): self.visible = False

    def show(self): self.visible = True
