'''https://leetcode.com/submissions/detail/330365307/'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, res= 0, 0
        for i in nums:
            if cnt == 0:
                res = i
            cnt += (1 if i == res else -1)

        return res
            

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]