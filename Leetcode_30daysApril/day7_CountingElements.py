'''Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.'''

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        arr.sort()
        for i in arr:
            if i+1 in arr:
                count+=1
        return count
                