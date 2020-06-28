import bisect
import time
#using fenwick tree
class FenwickTree:
    def __init__(self, n):
        self.BIT = [0] * (n+1)
    
    def sum(self, n):
        rv = 0
        while n > 0:
            rv += self.BIT[n]
            n -= n & -n
        return rv
    
    def increment(self, n):
        while n < len(self.BIT):
            self.BIT[n] += 1
            n += n & -n
            
class Solutionx:
    def countRangeSum(self, nums, lower, upper):
        sums = [0] * (len(nums)+1)
        for i, n in enumerate(nums):
            sums[i+1] = sums[i] + n
        sortedSums = sorted(sums)
        ranks = {s: i+1 for i, s in enumerate(sortedSums)}
        ft = FenwickTree(len(sums))
        rv = 0
        for s in sums:
            rv += (ft.sum(bisect.bisect_right(sortedSums, s-lower)) -
                   ft.sum(bisect.bisect_left(sortedSums, s-upper)))
            ft.increment(ranks[s])
        return rv





'''
arr = [0]
    for num in nums:
        arr.append(arr[-1] + num)
    def bisect(l, h):
        m = (l + h) / 2
        if m == l:
            return 0
        count = bisect(l, m) + bisect(m, h)
        i = j = m
        for left in arr[l:m]:
            while i < h and arr[i] - left <  lower: i += 1
            while j < h and arr[j] - left <= upper: j += 1
            count += j - i
        arr[l:h] = sorted(arr[l:h])
        return count
    return bisect(0, len(arr))
'''
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

class Solution(object):
    @timeit
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        arr = [0] * (len(nums)+1)
        
        for i, n in enumerate(nums):
            arr[i+1] = arr[i] + n
        
        def bisect(l, h):
            m = l + (h - l) // 2
            
            if m == l:
                return 0

            count = bisect(l, m) + bisect(m, h)
            i = j = m

            for left in arr[l:m]:
                while i < h and arr[i] - left <  lower: 
                    i += 1
                while j < h and arr[j] - left <= upper: 
                    j += 1
                count += j - i

            arr[l:h] = sorted(arr[l:h])
            return count
        
        return bisect(0, len(arr))


ss = Solution()
ss.countRangeSum([-2,1,5],-2,2)