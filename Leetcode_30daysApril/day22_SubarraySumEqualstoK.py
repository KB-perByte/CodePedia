class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache, Sum = {0:1}, 0
        ans = 0
        for i, n in enumerate(nums):
            Sum = Sum + n
            if Sum-k in cache:
                ans += cache[Sum-k]
            if Sum in cache:
                cache[Sum] += 1
            else:
                cache[Sum] = 1
        return ans