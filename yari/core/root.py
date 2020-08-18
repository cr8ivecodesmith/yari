"""
Root Node

"""

__all__ = ('Root',)

from yari.core.nodebase import NodeBase


def root_finder(node):
    """Utility for getting the root node

    """
    if getattr(node, 'root_node', None):
        return node.root_node

    parent = node.parent
    if parent and getattr(parent, 'root_node', None):
        return parent.root_node
    else:
        for n in node.walk_reverse(loopback=True):
            if getattr(n, 'root_node', None):
                return n.root_node


class Root(NodeBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.node_id = 'root'
        self.root_node = self

    def add_widget(self, node, *args, **kwargs):
        super().add_widget(node, *args, **kwargs)
        node._root_node = self
        if hasattr(node, 'initialize'):
            node.initialize()
        self.broadcast('on_initialize', node)
