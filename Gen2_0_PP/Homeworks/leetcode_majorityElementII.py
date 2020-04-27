class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = []
        if nums==[]:
            return 
        if len(nums)==1:
            return nums
        if len(nums)<3:
            return list(set(nums))

        for x in set(nums):
            t = nums.count(x)
            if (t>len(nums)//3):
                d.append(x)
        return d