class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        origColor = image[sr][sc]
        if newColor == origColor: return image

        newimage = image
        rows = len(newimage)
        cols = len(newimage[0])
        
        def fillHelper(r,c):
            #up
            if r>0 and newimage[r-1][c] == origColor:
                newimage[r-1][c] = newColor
                fillHelper(r-1,c)
            #down
            if r<rows-1 and newimage[r+1][c] == origColor:
                newimage[r+1][c] = newColor
                fillHelper(r+1,c)
            #left
            if c>0 and newimage[r][c-1] == origColor:
                newimage[r][c-1] = newColor
                fillHelper(r,c-1)
            #right
            if c<cols-1 and newimage[r][c+1] == origColor:
                newimage[r][c+1] = newColor
                fillHelper(r,c+1)
        
        newimage[sr][sc] = newColor
        fillHelper(sr,sc)
        return newimage
        