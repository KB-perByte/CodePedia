# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def numNodes(ptr,k):
            if not ptr:
                return 0,False
            left, found = numNodes(ptr.left,k)
            if found:
                return left,found
            if left == k-1:
                return ptr.val, True
            right, found =  numNodes(ptr.right,k-left-1)
            if found:
                return right,found
            else:
                return left + right +1,False

        return numNodes(root,k)[0]
