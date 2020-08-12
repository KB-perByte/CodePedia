class Node(object):
    #__slots__ = 'data', 'left', 'right'
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree(object):
    def __init__(self, node):
        self.root = Node(node)

    def preOrder(self, root, tree):
        if root:
            tree += str(root.data) + '-'
            tree = self.preOrder(root.left , tree)
            tree = self.preOrder(root.right, tree)
        return tree

    def inOrder(self, root, tree):
        if root:
            tree = self.inOrder(root.left, tree)
            tree += str(root.data) + '>'
            tree = self.inOrder(root.right,tree)
        return tree
'''
            7
        3       4
    1       2 2     2    
'''
t = Tree(7)
t.root.left = Node(3)
t.root.right = Node(4)
t.root.left.left = Node(1)
t.root.left.right = Node(2)
t.root.right.left = Node(2)
t.root.right.right = Node(2)
print(t)
print(t.preOrder(t.root, ''))
print(t.inOrder(t.root, ''))
