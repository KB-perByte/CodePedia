class Node:
    __slots__ = '_data','_next'

    def __init__(self, data = None, next = None) -> None:
        self._data = data
        self._next = next

class LinkedLStack:

    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def is_empty(self):
        return True if self._size == 0 else False

    def push(self, data):
        _node = Node(data, self._head)
        self._head = _node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise 'Stack Empty'
        ans = self._head
        self._head = self._head._next
        self._size -= 1
        return ans

    def top(self):
        if self.is_empty():
            raise 'Stack Empty'
        print(self._head._data)
        return self._head._data

    def view(self):
        temp = self._head
        while temp._next:
            print(temp._data, end = ' -> ')
            temp = temp._next
        else:
            print(temp._data)


ll = LinkedLStack()
ll.push(1)
ll.push(2)
ll.push(3)
ll.top()
ll.view()
ll.pop()
ll.view()