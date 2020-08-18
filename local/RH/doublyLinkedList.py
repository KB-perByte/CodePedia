class Node:
    __slots__ = 'data', 'prev', 'next', 'size'

    def __init__(self, prev = None, data = None, next = None ) -> None:
        self.prev = prev
        self.data = data
        self.next = next
        #self.size += 1
    
class DoublyLinkedList:
    __slots__ = 'head', 'tail'

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertDL(self, data):
        node = Node(None, data, None)

        if not self.head:
            self.head = self.tail = node
            self.head.prev = None
            self.head.next = None

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        
    def printLL(self):
        curr = self.head
        dLL = ''
        while curr:
            dLL += str(curr.data) + ' -> '
            curr = curr.next
        else:
            return False

dd = DoublyLinkedList()
dd.insertDL(1)
dd.insertDL(2)
dd.insertDL(3)
dd.insertDL(4)
dd.insertDL(5)
dd.insertDL(6)
print(dd.printLL())

            
