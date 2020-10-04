class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        visited = [False]*len(nums)
        res = []
        def dfs(path):
            print(path)
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    print("i: ", i)
                    if i > 0 and nums[i] == nums[i - 1] and visited[i-1]==False:
                        continue
                    if visited[i] == False:
                        print("in visited")
                        visited[i] = True
                        dfs(path + [nums[i]])
                        visited[i] = False
        dfs([])
        return res
        
