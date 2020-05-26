#https://ideone.com/LrtIzT
#recusion

class Solution(object):
    def maxUncrossedLines(self, A, B):
        lst = [ [-1]*(len(B)+1) for i in range(int(len(A))+1) ]

        def helper(i,j):
            if i==-1 or j==-1:
                return 0

            if lst[i][j]!=-1:
                return( lst[i][j] ) 

            if A[i]==B[j]:
                lst[i][j]= max( 1+helper(i-1,j-1), helper(i-1,j), helper(i,j-1) )

            else:
                lst[i][j]= max( helper(i-1,j), helper(i,j-1) )
                
            return(lst[i][j])

        return(helper(int(len(A))-1,len(B)-1))
        
sn =  Solution()
print(sn.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))

