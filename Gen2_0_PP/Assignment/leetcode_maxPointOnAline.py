import math
from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):       
        if len(points) <= 2:
            return len(points)
        
        result = 0
        
        for i in range(len(points)):
            map = defaultdict(lambda: defaultdict(int))
            overlap = 0
            most_points_on_same_line = 0
            
            for j in range(i+1, len(points)):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                
                if (x == 0 and y == 0):
                    overlap += 1
                    continue
                
                gcd = math.gcd(x, y)
                if (gcd != 0):
                    x //= gcd
                    y //= gcd
                
                # Normalize (always make y positive if possible then x if possible.)
                if y == 0 and x < 0:
                    x *= -1
                if y < 0:
                    x *= -1
                    y *= -1            
                
                map[x][y] += 1
                
                most_points_on_same_line = max(most_points_on_same_line, map[x][y])
        
            result = max(result, most_points_on_same_line+overlap+1)
        
        return result 