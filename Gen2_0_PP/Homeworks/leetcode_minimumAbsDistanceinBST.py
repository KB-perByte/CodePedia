# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = [None]
        pre = float('-inf')
        minimum = float('inf')
        while stack:
            while root:
                stack.append(root)
                root = root.left
        
            x = stack.pop()
            if x:
                minimum = min(abs(x.val - pre), minimum)  
                pre = x.val
                if x.right:
                    root = x.right 
        return minimum