'''https://leetcode.com/submissions/detail/330882329/'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        h, w = len(matrix), len(matrix[0])
        self.integral_image = [ [ 0 for _ in range(w) ] for _ in range(h) ]
        for y in range(h):
            summation = 0
            for x in range(w):
                summation += matrix[y][x]
                self.integral_image[y][x] = summation
                if y > 0:
                    self.integral_image[y][x] += self.integral_image[y-1][x]
                    
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right    = self.integral_image[row2][col2]
        bottom_left     = self.integral_image[row2][col1-1] if col1 >= 1 else 0
        top_right       = self.integral_image[row1-1][col2] if row1 >= 1 else 0
        top_left        = self.integral_image[row1-1][col1-1] if col1 >= 1 and row1 >=1 else 0
        return bottom_right - bottom_left - top_right + top_left