class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, n = 0, 0, len(nums)
        while(j<n):
            nums[i] = nums[j]
            while(j<n and nums[j]==nums[i]): j += 1
            i+=1
        return i