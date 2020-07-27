class Solution:
     def findMin(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        l, r = 0, n-1
        
        while r - l > 1:
            m = l + (r-l)//2                        
            			
            if nums[l] <= nums[m] < nums[r] or nums[l] < nums[m] <= nums[r]: return nums[l]
            
            if nums[m] < nums[m-1]: return nums[m]
            
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[l]:
                r = m-1
            else:
                return min(self.findMin(nums[l:m]), self.findMin(nums[m:r+1]))

        return min(nums[l:r+1])