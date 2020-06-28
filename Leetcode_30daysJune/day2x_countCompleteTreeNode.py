# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def f(r):
    if r==None:return
    global a;a+=1
    f(r.left);f(r.right)
a=0
class Solution:
    def countNodes(self, r: TreeNode) -> int:
        global a;a=0;f(r);return a 