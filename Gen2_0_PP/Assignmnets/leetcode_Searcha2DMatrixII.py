class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        count = -1 
        for z in matrix:            
            while z and z[count] > target and count + len(z):
                count -= 1                
            if z and z[count] == target:
                    return True

        return False