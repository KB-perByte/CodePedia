class Solution:
    def subsets(self, nums):
        subsets = []
        
        def generateSubsets(index, nums, current, subsets):
            subsets.append(current[:])
            for i in range(index, len(nums)):
                current.append(nums[i])
                generateSubsets(i + 1, nums, current, subsets)
                current.remove(current[-1])
                
        generateSubsets(0, nums, [], subsets)
        return subsets