class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        def perm(nums,start):
            if start==len(nums)-1:
                ans.append(nums) 
                return
            for j in range(start,len(nums)):
                nums[j],nums[start]=nums[start],nums[j] 
                perm(nums[:],start+1)  
        perm(nums,0)
        return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            yield nums
        elif n == 2:
            yield from [nums, nums[::-1]]
        else:
            for i, k in enumerate(nums):
                rem = nums[:i] + nums[i+1:]
                for perm in self.permute(rem):
                    yield [k] + perm