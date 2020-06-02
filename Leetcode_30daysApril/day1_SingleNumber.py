'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def powerOfList(nums):
            res = {i : nums.count(i) for i in set(nums)}
            return res
        res = powerOfList(nums)
        
        for k, v in res.items():
            if v == 1:
                return k  
        