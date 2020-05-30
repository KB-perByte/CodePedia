class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0, curr = []):
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

sols = Solution()
print(sols.subsets([1,2,3]))
print(sols.subsets('BAC'))


class Solution2: #USING PROPER BACKTRACKING
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