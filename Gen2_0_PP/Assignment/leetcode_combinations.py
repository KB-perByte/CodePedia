class Solution:
    def func(self, nums: List[int], k : int):
        n = len(nums)
        if k == 1:
            return [ [num] for num in nums ]
        res = []
        for i in range(n):
            x = nums[i]
            combs = self.func(nums[i+1:], k-1)
            for comb in combs:
                res.append([x] + comb)
        return res
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x+1 for x in range(n)]
        return self.func(nums, k)  