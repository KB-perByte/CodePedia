'''Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root, ans): 
            if (root == None): 
                return 0
            
            left_height = height(root.left, ans)  
            right_height = height(root.right, ans)  
            ans[0] = max(ans[0], 1 + left_height + 
                                     right_height)  
            return 1 + max(left_height, 
                           right_height)
        
        if (root == None):  
            return 0
        ans = [-999999999999] 
        height_of_tree = height(root, ans)  
        return ans[0]-1
