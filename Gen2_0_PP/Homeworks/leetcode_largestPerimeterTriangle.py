class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        A.reverse()
        for i in range(len(A) - 2):
            if A[i + 1] + A[i + 2] > A[i]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0