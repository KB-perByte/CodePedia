# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        val_to_node = {root.val: root}  # value to nodes at current depth
        node_to_parent = {root: None}
        while True:
            x_node = val_to_node.get(x, None)
            y_node = val_to_node.get(y, None)
            if x_node is not None and y_node is not None:
                return node_to_parent[x_node] != node_to_parent[y_node]
            if x_node is not None or y_node is not None:
                return False
            new_val_to_node = {}
            for node in val_to_node.values():
                if node.left:
                    node_to_parent[node.left] = node
                    new_val_to_node[node.left.val] = node.left
                if node.right:
                    node_to_parent[node.right] = node
                    new_val_to_node[node.right.val] = node.right
            val_to_node = new_val_to_node