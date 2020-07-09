def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3: return []
        result = []
        nums.sort()
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                j,k = i+1, n-1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]: j += 1
                        while j < k and nums[k] == nums[k-1]: k -= 1
                        j, k = j+1, k-1
                    elif sum < 0: j += 1
                    else: k -= 1
        return result
