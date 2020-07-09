# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.d = [[]]
        def f(l,p,r):
            if r:
                if len(self.d)<=l:
                    self.d.append([p])
                else:
                    self.d[l].append(p)
                f(l+1,2*p,r.left)
                f(l+1,2*p+1,r.right)
        f(0,0,root)
        return max(max(d) - min(d) + 1 for d in self.d )