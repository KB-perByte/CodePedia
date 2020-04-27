class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, j, steps = 0, 1, 0
        while j < len(nums):
            endj = min(nums[i]+i+1, len(nums))
            while j < endj:
                if nums[j] + j > nums[i] + i: i = j
                j += 1
            steps += 1
        return steps

##breaks with TLE
# 
# 
# try2
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        debit = 0
        for i in reversed(nums[:-1]):
            debit += 1
            if i - debit >= 0:
                debit = 0
        return debit <= 0     