class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node is None:
        return "*"
    else:
        return node.val + "," + serialize(node.left) + "," + serialize(node.right)

def deserialize(s):
    return deserialize_l(s.split(","))

def deserialize_l(s):
    if s[0] == "*":
        s.pop(0)
        return None
    else:
        n = Node(s[0])
        s.pop(0)
        n.left = deserialize_l(s)
        n.right = deserialize_l(s)
        return n
