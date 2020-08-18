class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix: 
            return 0
        
        res, histogram = 0, [0] * (len(matrix[0]) + 2)
        
        for row in matrix:
            for i, val in enumerate(row):
                if val == '0':
                    histogram[i + 1] = 0
                else:
                    histogram[i + 1] += 1
                    
            res = max(res, self.maxInHistogram(histogram))
        
        return res
        
        
    def maxInHistogram(self, hist) -> int:
        res, stack = 0, []
        
        for i, h in enumerate(hist):
            
            while stack and hist[stack[-1]] > h:
                j = stack.pop()
                res = max(res, (i - stack[-1]-1) * hist[j])
            
            stack.append(i)
        
        return res

f = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
ss = Solution()
ss.maximalRectangle(f)