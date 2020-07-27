class Solution:
    def addDigits(self, num: int) -> int:
        l = list(str(num))
        l = list(map(int, l))
        num = sum(l)
        if len(str(num)) > 1:
            num = self.addDigits(num)
        return num