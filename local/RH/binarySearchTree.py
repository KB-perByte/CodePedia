


class Node:
    __slots__ = 'left','data','right'

    def __init__(self, data = None):
        self.left = None
        self.data = data
        self.right = None 

class BST(Node):
    __slots__ = 'root'
    def __init__(self) -> None:
        super().__init__()
        self.root = None

    def _lazyload(self):
        from queue import Queue
        self.queue = Queue

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
           self._insert(data, self.root)

    def _insert(self, data, curr_ndoe):
        if data < curr_ndoe.data:
            if curr_ndoe.left is None:
                curr_ndoe.left = Node(data)
            else:
                self._insert(data, curr_ndoe.left)
        elif data > curr_ndoe.data:
            if  curr_ndoe.right is None:
                curr_ndoe.right = Node(data)
            else:
                self._insert(data, curr_ndoe.right)
        else:
            assert "No duplicates allowed"

    def find(self, data):
        isfound = None
        if self.root:
            isfound = self._find(data, self.root)
        return isfound

    def _find(self, data, curr_node):
        if data == curr_node.data:
            return True
        elif data < curr_node.data:
            if curr_node.left == None:
                return False
            else:
                return self._find(data, curr_node.left)
        elif data > curr_node.data:
            if curr_node.right == None:
                return False
            else:
                return self._find(data, curr_node.right)
        
    def levelOrderTrav(self, data):
        self._lazyload()



    def _levelOrder(self, data, curr):
        if data:
            self.queue.put(data)
        temp = self.queue.get()
        if temp.left:
            self.queue.put(temp.left)
        if temp.right:
            self.queue.put(temp.right)
            
        




bs = BST()
print(BST.__mro__)
bs.insert(9)
bs.insert(10)
bs.insert(20)
bs.insert(5)

bs.insert(3)
bs.insert(1)
bs.insert(5)
bs.insert(5)

bs.insert(6)
bs.insert(11)
bs.insert(32)
bs.insert(51)
print(bs.find(51))