'''
Advanced
1. For a linked list perform the following functions.
a. Reverse the link in single link list
b. Reverse the link using recursion
c. Reverse the link using stack.
'''

class Node: 

    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    def reverseUtil(self, curr, prev): 
        if curr.next is None : 
            self.head = curr  
            curr.next = prev 
            return 
        next = curr.next 
        curr.next = prev 
        self.reverseUtil(next, curr)  

    def reverseRecusion(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 
    
    def reverseStack(self,head): 
        stk = [] # a stack basically print by -1
        ptr = head 
        while (ptr != None):  
            stk.append(ptr) 
            ptr = ptr.next
        return stk
