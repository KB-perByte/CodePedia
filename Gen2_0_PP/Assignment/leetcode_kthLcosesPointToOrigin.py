class Solution:
    def get_tuple(self, x, y):
        val = -(x*x + y*y)
        point = (x,y)
        return (val, point)
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []        
        heap = []
        for i in range(K):
            heapq.heappush(heap, self.get_tuple(points[i][0], points[i][1]))
        
        for i in range(K, len(points)):
            tup = self.get_tuple(points[i][0], points[i][1])
            heapq.heappushpop(heap, tup)
        
        for item in heap:
            res.append(item[1])
        
        return res