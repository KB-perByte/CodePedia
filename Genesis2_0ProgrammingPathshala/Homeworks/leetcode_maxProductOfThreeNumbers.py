'''https://leetcode.com/submissions/detail/327546450/'''

import sys 
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if (nums[0]*nums[1]) > (nums[n-2] * nums[n-3]):
            return nums[0]*nums[1]*nums[n-1]
        else:
            return nums[n-1]*nums[n-2]*nums[n-3]