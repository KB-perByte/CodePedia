class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mask = 1
        for i in range(32):
            bit0 = 0
            for num in nums:
                if num & mask:
                    bit0 += 1
            res += bit0 * (len(nums) - bit0)
            mask <<= 1
        return res