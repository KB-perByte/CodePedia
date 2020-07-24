from functools import reduce
from operator import xor
class Solution:
    def singleNumber(self, nums):
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)



ss= Solution()
ss.singleNumber([1,1,2,4,2,4,3,5])