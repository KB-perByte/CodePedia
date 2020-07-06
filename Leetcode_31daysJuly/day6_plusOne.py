class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        e = digits[-1]
        if e != 9 :
            digits[-1] = e + 1
            return digits
        else :
            if len(digits) ==  1 :
                return [ 1, 0]
            return self.plusOne(digits[ : len(digits) - 1]) + [0]