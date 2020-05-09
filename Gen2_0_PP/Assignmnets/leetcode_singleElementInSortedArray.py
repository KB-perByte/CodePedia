class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l , r , n = 0, len(nums)-1 , len(nums)
        while l < r:
            mid = (l + r) //2
            if mid % 2 == 1:
                mid -= 1
            if mid + 1 == n or nums[mid + 1] != nums[mid]:
                r = mid
            else:
                l = mid + 2
        return nums[l]