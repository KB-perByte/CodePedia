class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        #build prefixSumArr sum 
        prefixSumArr = [[0]*(n+1) for _ in range(m+1)]
        
        for i, j in product(range(m), range(n)):
            prefixSumArr[i+1][j+1] = prefixSumArr[i+1][j] + prefixSumArr[i][j+1] - prefixSumArr[i][j] + mat[i][j]
        
        def below(k): 
            """reture true if there is such a sub-matrix of length k"""
            for i, j in product(range(m+1-k), range(n+1-k)):
                if prefixSumArr[i+k][j+k] - prefixSumArr[i][j+k] - prefixSumArr[i+k][j] + prefixSumArr[i][j] <= threshold: return True
            return False 
                
        #binary search
        lo, hi = 1, min(m, n)
        while lo <= hi: 
            mid = (lo + hi)//2
            if below(mid): lo = mid + 1
            else: hi = mid - 1
            
        return hi