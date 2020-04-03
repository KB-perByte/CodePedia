'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''
class Solution(object):
    def maxSubArray(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(a)
        max_here = 0
        high_end = 0

        for i in range(0, size): 
            high_end = high_end + a[i] 
            if high_end < 0: 
                high_end = 0
            elif (max_here < high_end): 
                max_here = high_end 

        return max_here 
