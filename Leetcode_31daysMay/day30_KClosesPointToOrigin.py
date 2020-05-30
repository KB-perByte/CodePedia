class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K > len(points):
            return None
        res, curr_res = [], 0
        for point in points:
            curr_res = math.sqrt( (0 - point[0])**2 + (0-point[1])**2 )
            res.append(curr_res)
        comb = zip(points, res)

        sorted_comb = sorted(comb, key = lambda x: x[1])
        values_back = [a for a, b in sorted_comb]
        
        return values_back[:K]

    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:K]