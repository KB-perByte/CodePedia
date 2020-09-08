class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                curr_node = q.popleft()
                if i < size - 1:
                    curr_node.next = q[0]
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        return root

''' way 2'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = collections.deque([root])
        while len(q) > 0:
            size = len(q)
            prev = None
            for _ in range(size):
                node = q.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node
            prev.next = None
        return root