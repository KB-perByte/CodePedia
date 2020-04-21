import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2:
            return 0
        minn, maxn = min(nums), max(nums)
        gap = int(ceil((maxn-minn)/float(N-1)))
        bucket = [[None, None] for elements in range(N-1)]
        for i in nums:
            if i == maxn:
                continue
            pos = int((i-minn)/gap)
            bucket[pos][0] = min(bucket[pos][0], i) if bucket[pos][0] else i
            bucket[pos][1] = max(bucket[pos][1], i) if bucket[pos][1] else i
        maxg, prev_max = gap, bucket[0][1]
        for b in bucket:
            if b[0] == None and b[1] == None:
                continue
            else:
                maxg = max(maxg, b[0]-prev_max)
                prev_max = b[1]
        if prev_max:
            maxg = max(maxg, maxn-prev_max)
        return maxg