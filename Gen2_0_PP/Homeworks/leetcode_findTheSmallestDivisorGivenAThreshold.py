#inary serach mininmize on decreasing array
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def funct(divisor):
            return sum(math.ceil(n / divisor) for n in nums)
            
        l, h = 1, max(nums)
        while l < h:
            m = (l + h) // 2
            if funct(m) > threshold:
                l = m + 1
            else:
                h = m
        return h