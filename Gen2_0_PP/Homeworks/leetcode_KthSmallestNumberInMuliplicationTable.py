class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 0, m * n
        while lo < hi: 
            mid = (lo + hi) // 2
            if self.fnc(m, n, k, mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
        
    def fnc(self,m, n, k, p):
        res = 0
        for i in range(1, m+1):
            res += min(n, p//i)
        return res < k