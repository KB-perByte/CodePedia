class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n, 2))
        
        for M in range(m_max, 1, -1):
            k = int(n**(1/M))
            if (k**(M+1) - 1)  == n*(k-1):
                return str(k)
        return str(n-1)

class Solution2:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        M = len(bin(n)) - 2
        while M > 0:
            low, high = 2, n - 1
            while low <= high:
                mid = (low + high) // 2
                res = (mid ** M - 1) // (mid - 1)
                if res == n: return str(mid)
                elif res < n: low = mid + 1
                else: high = mid - 1
            M -= 1
        return str(n) 