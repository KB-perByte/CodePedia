class Solution:
    def solveSudoku(self, m: List[List[str]]) -> None:
        self.v = { val for i in range(9) 
                                for j in range(9)
                                    for val in [(i,m[i][j]),(m[i][j],j),(i//3,j//3,m[i][j])]} 
        def helper(i,j):
            if i==9: return 1
            if j==9: return helper(i+1,0)
            if m[i][j]!='.': return helper(i,j+1)
            for k in range(1,10):
                k = str(k)
                if not ({(i,k),(k,j),(i//3,j//3,k)} & self.v):
                    m[i][j]=k
                    self.v |= {(i,k),(k,j),(i//3,j//3,k)}
                    if helper(i,j+1):
                        return 1
                    self.v -= {(i,k),(k,j),(i//3,j//3,k)}
                    m[i][j]='.'
        helper(0,0)