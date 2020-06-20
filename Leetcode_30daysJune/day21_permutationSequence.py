class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        nums = [i for i in range(1,n+1)]
        for i in range(n-1,0,-1):
            base = math.factorial(i)
            current = 0
            while k > base:
                k -= base
                current += 1
            res += str(nums[current])
            nums.pop(current)
        res += str(nums[0])
        return res