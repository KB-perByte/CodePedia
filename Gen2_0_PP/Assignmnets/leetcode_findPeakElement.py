class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while(l<r):
            m = (l+r)//2
            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m
        return l