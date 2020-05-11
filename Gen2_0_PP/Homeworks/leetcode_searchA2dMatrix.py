class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        if len(matrix) == 0:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows*cols -1
        while (left <= right):
            mid = left + (right -left)//2
            # Find row and col number
            row, col = mid//cols, mid%cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid-1
            else:
                left = mid+1
        return False