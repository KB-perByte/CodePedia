class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        combined = sorted(A + B, key=itemgetter(0))
        intersection = []
        currentEnd = -1

        for start, end in combined:
            if start <= currentEnd:
                intersection.append([start, min(currentEnd, end)])
            currentEnd = max(currentEnd, end)        

        return intersection