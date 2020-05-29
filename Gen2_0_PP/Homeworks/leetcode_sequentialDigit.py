'''https://leetcode.com/submissions/detail/345863533/'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.helper(res, 0, low, high, i)
        
        res.sort()
        return res            
         
    def helper(self, res, curr, low, high, digit):
        if curr > high: return
        if low <= curr:
            res.append(curr)
    
        if digit > 9: return
        self.helper(res, 10*curr + digit, low, high, digit+1)