"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        cur = head
        while True:
            if cur is None and len(stack) == 0:
                break
                                           
            if cur.child is not None:
                if cur.next:
                    stack.append(cur.next)
                temp = cur.child
                cur.child = None
                cur.next = temp
                temp.prev = cur
                cur = temp
            else:
                if cur.next is None and  len(stack) != 0:
                    temp = stack.pop()
                    cur.next = temp
                    temp.prev = cur
                    cur = temp
                else:
                    cur = cur.next
                
        return head  