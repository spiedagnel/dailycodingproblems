from unittest import TestCase

from binaryTreeSerialization.solution import Node, serialize, deserialize


class TestSerialize(TestCase):

    def test_serialize_None(self):
        self.assertEqual(serialize(None), '*')

    def test_serialize_single_node(self):
        node = Node('root')
        self.assertEqual(serialize(node), 'root,*,*')

    def test_serialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(serialize(node), 'root,left,left.left,*,*,*,right,*,*')

    def test_deserialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')