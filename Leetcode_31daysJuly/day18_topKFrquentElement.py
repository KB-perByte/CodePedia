
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dd = defaultdict(int)
        for i in nums:
            dd[i] += 1
            
        print(dd)
        
        return [x[0] for x in sorted(dd.items() , key=lambda x: -x[1])[:k]]
     