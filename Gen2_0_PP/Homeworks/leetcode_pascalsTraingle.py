class Solution(object):
    def generate(self, A):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascals_triangle = []

        for i in range(A):
            pascals_triangle.append([1]*(i+1))
            
        for i in range(2,A):
            for j in range(1,i):
                pascals_triangle[i][j] = pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j]
    
        return pascals_triangle