class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A =[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.A:
            self.A.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.A:
            return self.A[-1]
        else:
            return None
            
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.A:
            return min(self.A)
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
