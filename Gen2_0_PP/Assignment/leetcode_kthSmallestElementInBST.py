# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def do(main):
			if main==None or self.ans!=None:
				return 
			do(main.left)
			self.count-=1
			if self.count==0:
				self.ans=main.val
			do(main.right)
		self.count=k
		self.ans=None
		do(root)
		return self.ans