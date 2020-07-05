# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
    
        Out_temp, deq = [], deque([[root, 0]])
    
        while deq:
            elem = deq.popleft()
            Out_temp.append([elem[0].val, elem[1]])
            if elem[0].left:
                deq.append([elem[0].left, elem[1] + 1])
            if elem[0].right:
                deq.append([elem[0].right, elem[1] + 1])

        Out = [[Out_temp[0][0]]]
        for i in range(1, len(Out_temp)):
            if Out_temp[i][1] == Out_temp[i-1][1]:
                Out[Out_temp[i][1]].append(Out_temp[i][0])
            else:
                Out.append([Out_temp[i][0]])

        return Out[::-1]