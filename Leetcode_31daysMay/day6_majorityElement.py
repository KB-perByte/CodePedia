class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, element = 0 , None
        
        for i, n in enumerate(nums):
            if cnt == 0:
                element = n
            if element == n:
                cnt+=1
            else:
                cnt-=1
        return element
            
        