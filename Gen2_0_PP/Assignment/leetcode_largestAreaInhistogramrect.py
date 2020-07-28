class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
         def getNSR(heights):
            s = []
            res = []
            
            for i in range(len(heights)-1,-1,-1):
                if len(s)==0:
                    res.append(len(heights))
                elif s[-1][1] < heights[i]:
                    res.append(s[-1][0])
                elif s[-1][1] >= heights[i]:
                    while len(s)>0 and s[-1][1] >= heights[i]:
                        s.pop()
                    if len(s) == 0:
                        res.append(len(heights))
                    else:
                        res.append(s[-1][0])
                        
                s.append((i,heights[i]))
            
            res.reverse()
            return res
        
        def getNSL(heights):
            s = []
            res = []
            
            for i in range(len(heights)):
                if len(s)==0:
                    res.append(-1)
                elif s[-1][1] < heights[i]:
                    res.append(s[-1][0])
                elif s[-1][1] >= heights[i]:
                    while len(s)>0 and s[-1][1] >= heights[i]:
                        s.pop()
                    if len(s) == 0:
                        res.append(-1)
                    else:
                        res.append(s[-1][0])
                        
                s.append((i,heights[i]))
                
            return res
        
        if len(heights)==0:
            return 0
        
        area = []
        NSR = getNSR(heights)
        NSL = getNSL(heights)
        
        width = [NSR[i]-NSL[i]-1 for i in range(len(heights))]
        
        area = [heights[i]*width[i] for i in range(len(heights))]  
		
        return max(area)   