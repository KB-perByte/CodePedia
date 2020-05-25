class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        return self.permuteUniqueSorted(nums)

    def permuteUniqueSorted(self, nums):
        permutations = []

        if len(nums) <= 1:
            permutations.append(nums)
            return permutations

        # Take one element at a time from nums, and make permutations with the rest.
        for i in range (len(nums)):
            # Avoid duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # nums[:i] + nums[i+1:] is equivalent to nums without nums[i]
            sub_permutations = self.permuteUniqueSorted(nums[:i] + nums[i+1:])
            for sub_permutation in sub_permutations:
                permutations.append([nums[i]] + sub_permutation)
        return permutations