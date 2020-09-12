# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.ans = 0
    
        def helper(node):
            if not node:
                return float('inf'), float('-inf'), 0
            small_left, big_left, total_left = helper(node.left)
            small_right, big_right, total_right = helper(node.right)
            if big_left < node.val < small_right:
                self.ans = max(self.ans, total_left+total_right+node.val)
                return min(small_left, node.val), max(big_right, node.val), total_left+total_right+node.val
            return float('-inf'), float('inf'), 0

        helper(root)
        return self.ans