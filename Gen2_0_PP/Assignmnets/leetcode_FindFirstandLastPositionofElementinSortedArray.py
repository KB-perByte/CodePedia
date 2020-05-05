class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return (-1, -1)
       
        def find_left(nums, l, r, target):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target: l = mid + 1
                
                elif nums[mid-1] < target: return mid
               
                else: r = mid - 1
            return l
        
      
        def find_right(nums, l, r, target):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] > target: r = mid - 1
              
                elif nums[mid+1] > target: return mid
          
                else: l = mid + 1
            return r
        
	
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target: l = mid + 1
            elif nums[mid] > target: r = mid - 1
            else: 
                return [find_left(nums, 0, mid, target), find_right(nums, mid, len(nums)-1, target)]
        return (-1, -1)
        