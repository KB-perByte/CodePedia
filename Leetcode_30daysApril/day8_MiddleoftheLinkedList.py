'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None): 
            return None
        
        ptr1_node = head 
        ptr2_node = head 
        prev = None
        while(ptr2_node != None and ptr2_node.next != None): 
            prev = ptr1_node 
            ptr1_node = ptr1_node.next
            ptr2_node = ptr2_node.next.next
            
        return ptr1_node
        
