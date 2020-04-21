class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return []

        x0,x1 = 0, len(matrix[0])
        y0,y1 = 0, len(matrix)
        res = []
        while x0<x1 and y0<y1:
            #-----> top traverse
            for i in range(x0,x1):
                res.append(matrix[y0][i])
            #right side traverse 
            for j in range(y0+1,y1-1): #not fixing zero so that it can handle a non sqare marix
                res.append(matrix[j][x1-1])
            if y1!=y0+1: #right to left lower array
                for i in range(x1-1,x0-1,-1):
                    res.append(matrix[y1-1][i])
            if x0!=x1-1: #bottom up 
                for j in range(y1-1-1,y0,-1):
                    res.append(matrix[j][x0])
            x0+=1
            y0+=1
            x1-=1
            y1-=1
        return res
        