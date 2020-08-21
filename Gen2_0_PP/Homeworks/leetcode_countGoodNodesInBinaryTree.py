# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count =0
        def goodNodes(root, max_so_far):
            if not root:
                return
            if root.val >= max_so_far:
                self.count +=1
                max_so_far = root.val
            goodNodes(root.left, max_so_far)
            goodNodes(root.right, max_so_far)
            
        goodNodes(root,float('-inf'))
        return self.count