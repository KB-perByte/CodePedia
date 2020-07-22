# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        list: ans = []
        if not root: return ans
        
        def rec(root, height):
            
            if not root: return
            if len(ans) == height:
                ans.append([])
            if height%2 == 0:
                ans[height].append(root.val)
            else:
                ans[height].insert(0,root.val)  
            rec(root.left, height+1)
            rec(root.right, height+1)
        
        rec(root,0)
        return ans