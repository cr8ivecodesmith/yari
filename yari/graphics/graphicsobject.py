__all__ = ('GraphicsObject',)

from kivy.graphics.instructions import InstructionGroup


class GraphicsObject(InstructionGroup):

    def __init__(self, name=None, groups=None, **kwargs):
        super().__init__(**kwargs)
        self._name = name or ''
        self.groups = groups or set()
        assert (
            isinstance(self.groups, set)
        ), 'GraphicsObject.group must be a set object.'

    @property
    def name(self): return self._name
