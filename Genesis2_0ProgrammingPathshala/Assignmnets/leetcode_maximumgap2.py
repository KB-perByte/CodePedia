class Solution(object):
    def maximumGap(self, nums):
        nums = sorted(nums)
        if len(nums)<2:
            return 0
        x = 0
        
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])>x: x=abs(nums[i]-nums[i+1])
        return x