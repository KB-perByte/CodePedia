class Solution:
    # @param A : list of list of integers
    # @return an integer
    c = 0
    def uniquePathsIII(self, A):
        #find where 1 is and count -1's
        cnt = 0
        for x in range(len(A)):
            for y in range(len(A[0])):
                if A[x][y] == 1:
                    s_r = x
                    s_c = y
                elif A[x][y] == -1:
                    cnt += 1
        self.pathBacktracking(A, s_r, s_c, cnt)
        return self.c
        
        
    def pathBacktracking(self, A, r, c, cnt):
        if r < 0 or c < 0 or r == len(A) or c == len(A[0]) or A[r][c] == -1: #If index is out of boundary or if an element is already visited
            return
        if A[r][c] == 2:
            #If count of -1's is 1 lesser than all the elements in the array(because 2 is left)
            if cnt == len(A)*len(A[0])-1:
                self.c += 1
            return
        #set current index to -1 before going anywhere to not revisit
        #go up
        A[r][c] = -1
        self.pathBacktracking(A, r - 1, c, cnt + 1)
        A[r][c] = 0 #backtrack/reset
       
        #go down
        A[r][c] = -1
        self.pathBacktracking(A, r + 1, c, cnt + 1)
        A[r][c] = 0
        
        #go left
        A[r][c] = -1
        self.pathBacktracking(A, r, c - 1, cnt + 1)
        A[r][c] = 0

        #go right
        A[r][c] = -1
        self.pathBacktracking(A, r, c + 1, cnt + 1)
        A[r][c] = 0