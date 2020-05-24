class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j]=matrix[i][j] and min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
            #print(matrix)
            #print(len(matrix))
        #print(matrix)
        #print(len(matrix))
             
        return sum([sum(row) for row in matrix])
    