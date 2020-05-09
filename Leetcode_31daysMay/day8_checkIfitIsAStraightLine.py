class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if coordinates[1][0]-coordinates[0][0]!=0:
            k=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        else:
            k=0
        b=coordinates[0][1]-k*coordinates[0][0]
        for i in coordinates:
            if i[1]!=i[0]*k+b:
                return False
        return True