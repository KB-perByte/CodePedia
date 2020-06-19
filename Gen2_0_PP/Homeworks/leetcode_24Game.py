class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
		return abs(nums[0] - 24) < 0.01

	ans = False
	for i in range(len(nums)):
		for j in range(i):
			rest = []
			for k in range(len(nums)):
				if k != i and k != j:
					rest.append(nums[k])
			target = [
				nums[i] + nums[j], nums[i] - nums[j],
				nums[j] - nums[i], nums[i] * nums[j]
			]
			if nums[i]:
				target.append(nums[j] / float(nums[i]))
			if nums[j]:
				target.append(nums[i] / float(nums[j]))
			for t in target:
				ans = ans or self.judgePoint24(rest[:] + [t])
				if ans:
					return True
	return ans
