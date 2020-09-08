class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        s, dp, ret = [], [0], 0
        for i, e in enumerate(A):
            while s and A[s[-1]] >= e: s.pop()
            dp.append((i - (p := s[-1] if s else -1)) * e + dp[p + 1])
            ret = (ret + dp[-1]) % (10**9 + 7)
            s.append(i)
        return ret