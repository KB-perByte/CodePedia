# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        greater, smaller = (p.val, q.val) if p.val > q.val else (q.val, p.val)
        cur = root
        while cur is not None:
            if smaller < cur.val < greater or (cur.val == smaller) or (cur.val == greater):
                return cur
            if cur.val > greater:
                cur = cur.left
            else: # cur.val < smaller:
                cur = cur.right
        return None