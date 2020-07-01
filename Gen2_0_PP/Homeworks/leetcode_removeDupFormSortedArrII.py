class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        j,n=2,len(nums)-1
        while(j <= n):
            #print(nums[j],nums[n])
            if nums[j-2] == nums[j] and nums[j-1] == nums[j]:
                nums.append(nums.pop(j))
                n -= 1
            else:
                j += 1
        return n+1