# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_reverse(a, b):
            # return true iff `a` is a reversed tree of `b`
            if not a or not b: return not a and not b
            return a.val == b.val and is_reverse(a.left,b.right) and is_reverse(a.right,b.left) 

        if not root: return True
        return is_reverse(root.left, root.right)