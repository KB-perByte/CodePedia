class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        if not nums: return 0
        loopCntMax = 1
        for i in range(len(nums)):
            if nums[i] == -1 or nums[i] == i:
                continue
            start, prev, curr, cnt = i, nums[i], nums[i], 0
            while prev != start:
                prev, curr, cnt = curr, nums[curr], cnt+1
                nums[prev] = -1
            nums[prev] = -1
            loopCntMax = max(loopCntMax, cnt) 
        return loopCntMax