#Assignment (Arrays 1)
'''https://leetcode.com/submissions/detail/327189103/'''

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def compare(A1, A2):
            return arr[A1]-arr[A2] if arr[A1] != arr[A2] else A1-A2
        
        idxs = [i for i in xrange(len(arr))]
        result, max_i = 0, 0
        for i, v in enumerate(sorted(idxs, cmp=compare)):
            max_i = max(max_i, v)
            if max_i == i:
                result += 1
        return result

#debug
def maxChunksToSorted( arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def compare(A1, A2):
            return arr[A1]-arr[A2] if arr[A1] != arr[A2] else A1-A2
        
        idxs = [i for i in xrange(len(arr))]
        result, max_i = 0, 0
        for i, v in enumerate(sorted(idxs, cmp=compare)):
            max_i = max(max_i, v)
            if max_i == i:
                result += 1
        return result

maxChunksToSorted([1,0,2,3,4])


#option
class _Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        _min = len(arr)-1
        flag = False
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==len(arr)-1:
                flag = True
            if arr[i]<_min:
                _min = arr[i]
            if flag and _min == i:
                return self.maxChunksToSorted(arr[:i])+1