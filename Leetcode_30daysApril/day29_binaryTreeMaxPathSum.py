# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float('-inf')
        def sumTree(root):
            if root is None:
                return 0
            else:
                ls = max(sumTree(root.left), 0)
                rs = max(sumTree(root.right), 0)
                self.max = max(self.max, ls + rs + root.val)
                return max(ls, rs, 0) + root.val
        
        sumTree(root)
        return self.max
        