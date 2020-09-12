# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    tree=None
    def serialize(self, root: TreeNode) -> str:
        self.tree=root
        return str(root)
    def deserialize(self, data: str) -> TreeNode:
        return self.tree
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))