class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        MAX = 9999999
        l = MAX
        sum = 0
        step = False
        ini = 0
        for i in range(0, len(nums)):  
            sum += nums[i]    
            while sum >= s and ini <= i:
                l = min(l, i - ini + 1)
                if l == 1: return 1
                sum -= nums[ini]
                ini += 1
                step = True
                
            if step:
                sum -= nums[ini]
                ini += 1
            
        return l if l != MAX else 0
 