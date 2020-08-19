"""
Base Node

Only Node and Root should inherit this.

NOTES:

- Setting node_id value from kvlang doesn't take in effect. Even with
the event binding.

"""

__all__ = ('NodeBase',)

from collections import defaultdict

from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from yari.core.event import Event


def handle_node_id(this, val):
    if val in this.nodes:
        raise KeyError(
            f'node_id [{val}] already exists in node [{this}]!'
        )


class NodeBase(Event, Widget):

    node_id = StringProperty('')

    def __init__(self, **kwargs):
        self.nodes = {}
        self._node_last_id = defaultdict(int)

        self.create_event('on_initialize')
        self.create_event('on_add_node')
        self.create_event('on_remove_node')

        self.bind(node_id=handle_node_id)

        self.add_node = self.add_widget
        self.remove_node = self.remove_widget
        self.clear_nodes = self.clear_widgets

        super().__init__(**kwargs)

    def add_widget(self, node, *args, **kwargs):
        if not issubclass(node.__class__, NodeBase):
            node.node_id = ''

        node_id = node.node_id

        if not node_id:
            name = node.__class__.__name__.lower()
            self._node_last_id[name] += 1
            node_id = f'{name}{self._node_last_id[name]}'
            node.node_id = node_id

        self.nodes[node_id] = node
        super().add_widget(node, *args, **kwargs)

        self.broadcast('on_add_node', node)

    def remove_widget(self, node, *args, **kwargs):
        self.broadcast('on_remove_node', node)
        super().remove_widget(node, *args, **kwargs)

    def clear_widgets(self, nodes=None, *args, **kwargs):
        _nodes = nodes or self.children
        for node in _nodes:
            self.broadcast('on_remove_node', node)
        super().clear_widgets(nodes, *args, **kwargs)
