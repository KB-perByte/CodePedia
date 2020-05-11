class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        left,right = 0,l-1
        res = 0
        while right>=left:
            mid = (right+left)//2
            if citations[mid]>=l-mid:
                res = max(res,l-mid)
                right = mid-1
            else:
                left = mid+1
        return res