# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def helper(node):
            if not node: return True, head
            res, tail = helper(node.next)
            return res and node.val == tail.val, tail.next
        return helper(head)[0]