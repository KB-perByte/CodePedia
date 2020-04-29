class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        
        def compute_hcf(x, y):
            while(y):
                x, y = y, x % y
            return x
 
        x = nums[0]    
        for number in nums:
            x = compute_hcf(x, number)
        return x == 1