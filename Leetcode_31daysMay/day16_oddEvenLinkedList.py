# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_of_even = None  
        try:
            head_of_even = head.next       
        except AttributeError:
            return head
        cur_odd, cur_even = head, head_of_even
        while True:
            try:
                cur_odd.next = cur_odd.next.next
                cur_even.next = cur_even.next.next
                cur_odd, cur_even = cur_odd.next, cur_even.next
            except AttributeError:
                break
        cur_odd.next = head_of_even
        return head


def oddEvenList(self, head: ListNode) -> ListNode:
	if not head or not head.next:
		return head
	odd=head
	even=head.next
	even_head=even
	while even and even.next:
		odd.next=even.next
		odd=odd.next
		even.next=even.next.next
		even = even.next
	odd.next=even_head
	return head