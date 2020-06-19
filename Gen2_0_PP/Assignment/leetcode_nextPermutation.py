class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev_inplace(a, l, h):
            for i in range(0, (h - l + 1) // 2):
                a[l+i], a[h-i] = a[h-i], a[l+i]
                
        N = len(nums)
        i = N - 1
        while nums[i-1] >= nums[i] and i > 0:  i -= 1
        
        if i > 0:
            for k in range(len(nums) - 1, i - 1, -1):
                if nums[k] > nums[i-1]: break
            nums[k], nums[i-1] = nums[i-1], nums[k]
		
        rev_inplace(nums, i, N - 1)