class Node:
    def __init__(self ,data = None ,next = None):
        self.value = data
        self.next = next
    
class LinkedList:
    def __init__(self, head = None):
        self.head = None

    def insert_at_end(self, data):
        _data = Node(data, None)
        _node = self.head

        if self.head == None:
            self.head = _data
            return
        else:
            while _node.next:
                _node = _node.next
        
        _node.next = _data

    def insert_at_beginning(self, data):
        _data = Node(data, None)
        if self.head:
            temp = self.head
            self.head = _data
            self.head.next = temp
        else:
            self.insert_at_end(data)

    def print_LL(self):
        _node = self.head
        stLL = ''
        if _node:
            while _node.next:
                stLL += (str(_node.value) + ' -> ')
                _node = _node.next
            else:
                stLL += str(_node.value)
        print(stLL)
        return 'empty' if stLL == '' else stLL

    def delete_node_byValue(self, target):
        _node = self.head
        _prev = None
        while _node.value is not target:
            _prev = _node
            _node = _node.next
        if _node.next:
            _node.value = _node.next.value
            _node.next = _node.next.next
        else:
            _prev.next = None

    def reverse_ll(self, node):
        """ using  recusrion """
        if node == None or node.next == None:
            return node
        print('call stack for', str(node.value))
        res = self.reverse_ll(node.next)
        print('reversing ', str(node.value))
        node.next.next = node
        node.next = None
        self.head = res
        return res

    def reverse_iterative(self, node):
        """iterative approach """
        stack=[]
        while node:
            #node = node.next
            if node:
                stack.append(node.value)
            node = node.next

        while stack:
            print(stack[-1])
            #self.head = stack[-1]
            self.insert_at_beginning(stack.pop())


myll = LinkedList()
myll.print_LL()
myll.insert_at_end(1)
#myll.insert_at_end(2)
myll.insert_at_end(3)
#myll.insert_at_beginning(0)
#myll.insert_at_end(7)
myll.print_LL()
#myll.delete_node_byValue(7)
myll.print_LL()
myll.reverse_ll(myll.head)
myll.print_LL()
myll.reverse_iterative(myll.head)
myll.print_LL()