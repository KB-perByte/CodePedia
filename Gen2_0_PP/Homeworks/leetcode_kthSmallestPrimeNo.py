class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        lo, hi, n = 0, 1, len(A)
        while lo < hi:
            mi, j, p, q, cnt =  (lo + hi) / 2, 0, 0, 1, 0
            for i in range(n):
                while j < n and A[i] / A[j] > mi: j += 1
                if j < n and p / q < A[i] / A[j]: p, q = A[i], A[j]
                cnt += n - j
            if cnt > K: hi = mi
            elif cnt < K: lo = mi
            else: return [p, q]