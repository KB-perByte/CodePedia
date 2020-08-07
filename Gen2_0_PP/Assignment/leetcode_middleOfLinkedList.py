# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        x = head
        y = head
        while y and y.next:
            x = x.next
            y = y.next.next
        return x
    