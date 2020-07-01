class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = (int)(sqrt(2*n))
        sum = (int)(k*(k+1)/2)
        if sum > n: return k - 1
        return k