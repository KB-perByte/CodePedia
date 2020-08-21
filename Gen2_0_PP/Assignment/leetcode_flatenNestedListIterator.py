#Yield RH inportant questin

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
     def __init__(self, A):
        self.gen    = self.yielder(A)
        self.buffer = next(self.gen,None)
    
    def yielder(self,A):
        if type(A)==list or not A.isInteger():
		    B = A if type(A)==list else A.getList()
            for x in B:
                for y in self.yielder(x):
                    yield y
        else:
            yield A.getInteger()
    
	def next(self):
        a,self.buffer = self.buffer, next(self.gen,None)
        return a
    
	def hasNext(self):
        return self.buffer is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())