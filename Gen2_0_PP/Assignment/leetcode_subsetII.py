class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.ln = len(nums)
        if self.ln == 0:
            return self.res
        self.nums = sorted(nums)
        self.helper(0, [])

        return self.res

    def helper(self, idx, tmp):
        self.res.append(tmp)
        for i in range(idx, self.ln):
            if i > idx and self.nums[i] == self.nums[i-1]:
                continue
            self.helper(i+1, tmp + [self.nums[i]])
