'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #so, reverse and transpose
        for i in range(len(matrix)-1,0, -1):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] 
'''

# def rotate(matrix):
#     #so, reverse and transpose
#     for i in range(len(matrix)-1,0, -1):
#         for j in range(i):
#             matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
#         print(matrix[~i])
#     return matrix

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """                
        n = len(matrix)
        for level in range(0,n//2):            
            for i in range(level,n - level-1):
                tmp = matrix[level][i]
                for j in range(4):                
                    if j == 0:
                        #right
                        nxt_row = i
                        nxt_col = n - level - 1
                    elif j == 1:
                        #bottom
                        nxt_row = n - level - 1 
                        nxt_col = n - 1 - i
                    elif j == 2:
                        # left
                        nxt_row = n - 1 - i 
                        nxt_col = level
                    else:
                        # top
                        nxt_row = level
                        nxt_col = i 
                        
                    tmp_nxt = matrix[nxt_row][nxt_col]
                    matrix[nxt_row][nxt_col] = tmp
                    tmp = tmp_nxt

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))