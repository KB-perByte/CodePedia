class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val in nums:
            while val in nums:
                nums.remove(val)
            return len(nums)
        else: return


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)
        while start < end:
            if nums[start] == val:
                nums[start] = nums[end - 1]
                end -= 1
            else:
                start += 1
        return end