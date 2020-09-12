# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.running_sum = 0
        
    def convertBST(self, root):
        def dfs(node):
            if node:
                dfs(node.right)
                self.running_sum += node.val
                node.val = self.running_sum
                dfs(node.left)
            return node
        return dfs(root)