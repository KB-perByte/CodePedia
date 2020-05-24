class Solution(object):
    def combinationSum42(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dfs(idx, cur, memo):
            if cur == target:
                return 1
            if cur > target:
                return 0
            if (idx, cur) in memo:
                return memo[idx, cur]
            memo[idx, cur] = sum(dfs(i, cur + nums[i], memo) for i in range(n))
            return memo[idx, cur]
        n = len(nums)
        return dfs(0, 0, {})


    def combinationSum4(self, nums, target):
        def dfs(cur, memo):
            if cur == target:
                return 1
            if cur > target:
                return 0
            if cur in memo:
                return memo[cur]
            memo[cur] = sum(dfs(cur + nums[i], memo) for i in range(n))
            return memo[cur]
        n = len(nums)
        return dfs(0, {})
    
    def combinationSum42(self, nums, target):
        def dfs(idx, cur, memo):
            if idx == n:
                return 1 if cur == target else 0
            if cur > target:
                return 0
            if (idx, cur) in memo:
                return memo[idx, cur]
            memo[idx, cur] = dfs(idx + 1, cur, memo) + dfs(idx, cur + nums[idx], memo)
            return memo[idx, cur]
        n = len(nums)
        return dfs(0, 0, {})
    
    def combinationSum42(self, nums, target):
        store = [0]*(target+1)
        
        for i in range(target+1):
            count = 0
            for j in nums:
                if i-j == 0:
                    count += 1
                elif i-j > 0:
                    count += store[i-j]
            store[i] = count
            
        return store[target]