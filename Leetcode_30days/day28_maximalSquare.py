class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        x_arr = [[0] * len(matrix[0]) for x in range(len(matrix))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                else:
                    if x_arr[i][j-1] == 0:
                        width = 1
                    else:
                        width  = x_arr[i][j-1]+1
                    x_arr[i][j] = width
                for k in range(i,-1,-1):
                    width = min(width,x_arr[k][j])
                    max_area = max(max_area,min(i-k+1,width)*min(i-k+1,width))
        print(x_arr)
        return max_area
        