'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = [0] * len(nums)
        mul[-1]=nums[-1]
        for i in range(1,len(nums)):
            mul[len(nums)-i-1] = mul[len(nums)-i] * nums[len(nums)-i-1]
        output = [0]*len(nums)
        prefix = 1
        curr = 0
        while curr < len(output)-1:
            output[curr] = prefix * mul[curr+1]
            prefix *= nums[curr]
            curr +=1
        output[-1] = prefix
        return output