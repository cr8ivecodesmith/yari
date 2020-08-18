"""
Core Node

All other widgets should inherit this.

"""

__all__ = ('Node',)

from yari.core.nodebase import NodeBase
from yari.core.root import root_finder


class Node(NodeBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._root_node = None

    @property
    def root_node(self): return self._root_node

    def add_widget(self, node, *args, **kwargs):
        super().add_widget(node, *args, **kwargs)
        node._root_node = root_finder(node)
        if hasattr(node, 'initialize'):
            node.initialize()
        self.broadcast('on_initialize', node)

    def initialize(self): pass
