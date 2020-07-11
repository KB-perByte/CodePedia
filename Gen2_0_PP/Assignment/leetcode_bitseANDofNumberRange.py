class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bwSm = 0
        while m != n:
            m >>= 1
            n >>= 1
            bwSm += 1
        return m << bwSm
        