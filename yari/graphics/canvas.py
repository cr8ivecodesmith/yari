"""
Canvas Node

This is a node for drawing graphics.

"""

__all__ = ('Canvas',)

from collections import defaultdict

from yari.core import Node


class Canvas(Node):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_event('on_add_object')
        self.create_event('on_remove_object')

        self.objects = ({}, {}, {},)
        self._obj_last_id = defaultdict(int)

    def get_layer(self, layer=1):
        assert (
            0 <= layer <= 2
        ), 'Layer must be 0 for "before", 1 "middle", or  2 "after".'
        ltype = None
        if layer == 0:
            ltype = 'before'
        elif layer == 2:
            ltype = 'after'
        return getattr(self.canvas, ltype) if ltype else self.canvas

    def get(self, obj_name, layer=1):
        return self.objects[layer][obj_name]

    def get_objects(self, group=None, layer=1):
        if group:
            for obj in self.objects[layer].values():
                if group in obj.groups:
                    yield obj
        else:
            for obj in self.objects[layer].values():
                yield obj

    def add(self, obj, layer=1):
        canvas = self.get_layer(layer)
        objects = self.objects[layer]

        assert (
            obj.name not in objects
        ), (
            f'GraphicsObject name {obj.name} already exists in '
            f'layer {layer} of {self}.'
        )

        if not obj.name:
            cls_name = obj.__class__.__name__.lower()
            self._obj_last_id[cls_name] += 1
            obj._name = f'{cls_name}{self._obj_last_id[cls_name]}'

        canvas.add(obj)
        objects[obj.name] = obj
        self.broadcast('on_add_object', obj)

    def remove(self, obj_name, layer=1):
        canvas = self.get_layer(layer)
        obj = self.objects[layer].pop(obj_name)
        self.broadcast('on_remove_object', obj)
        canvas.remove(obj)
