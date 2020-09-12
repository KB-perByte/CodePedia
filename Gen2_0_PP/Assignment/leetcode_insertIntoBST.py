# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode( val )
            return root
        
        def helper( node: TreeNode, val: int) ->TreeNode:
            
            if val > node.val:
                
                if not node.right:
                    node.right = TreeNode( val )
                    return
                else:
                    helper(node.right, val)
            else:
                if not node.left:
                    node.left = TreeNode( val )
                    return
                else:
                    helper(node.left, val)
                
        
        helper(root, val)
        return root