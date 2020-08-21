# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []

        def helper(node):
            nonlocal count
            if node.left:  helper(node.left)          # 1
            if node.right: helper(node.right)         # 1
            if node.left:  node.val += node.left.val  # 2
            if node.right: node.val += node.right.val # 2
            count[node.val] += 1                      # 3

        count = collections.defaultdict(int)
        helper(root)

        max_freq = max(count.values())                                   # 4
        return [total for total in count if (count[total] == max_freq)]  # 4