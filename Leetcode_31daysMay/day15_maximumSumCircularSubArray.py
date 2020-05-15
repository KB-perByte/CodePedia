class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_so_far = min_so_far = min_ending_here = max_ending_here = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)    
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        if min_so_far == sum(A):
            return max_so_far
        else:
            return max(max_so_far,sum(A)-min_so_far)