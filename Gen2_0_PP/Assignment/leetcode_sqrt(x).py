class Solution:
    def mySqrt(self, x: int) -> int:
        root = x
        while root * root > x:
            root = (root + x // root) // 2
        return root
    