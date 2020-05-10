class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        cnt = [0] * (N + 1)
        for tst, tsd in trust:
            cnt[tsd] += 1
            cnt[tst] -= 1
        
        for i in range(1, N+1):
            if cnt[i] == N-1:
                return i
        
        return -1