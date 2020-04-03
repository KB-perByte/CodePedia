'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

'''
# def operation(n, iter):
#     
#     if n == 1:
#         return True
#     while n:
#         if iter <0:
#             return False
#         a += ((n%10)**2)
#         n = n//10
#     iter-=1
#     return operation(a,iter)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.solve(n,{})
    
    def solve(self,n,visited):
        if n == 1:
            return True
        if n in visited:
            return False
        visited[n]= 1
        n = str(n)
        l = list(n)
        l = list(map(int,l))
        temp = 0
        for i in l:
            temp += (i**2)
        return self.solve(temp,visited)

