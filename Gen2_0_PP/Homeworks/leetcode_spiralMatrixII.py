'''https://leetcode.com/submissions/detail/328450105/'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def fillSquare(r, c, s):
            nonlocal count
            if mat[r][c]:
                return 
            if n == 1:
                mat[r][c] = count
                return
            
            # Top
            mat[r][c:c+s] = range(count, count+s)
            count += s
            # Right
            for x in range(r+1, r+s):
                mat[x][c+s-1] = count
                count += 1
            # Bottom
            mat[r+s-1][c:c+s-1] = reversed(range(count, count+s-1))
            count += s-1
            # Left
            for y in reversed(range(r+1, r+s-1)):
                mat[y][c] = count
                count += 1
                
            fillSquare(r+1, c+1, s-2)
            
        if n == 0:
            return None
        
        mat = [[0 for _ in range(n)] for _ in range(n)] 
        count = 1 
        fillSquare(0, 0, n)
        return mat