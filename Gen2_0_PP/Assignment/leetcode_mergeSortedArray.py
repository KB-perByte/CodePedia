class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        num = []
        
        while i < m or j < n:
            val1 = nums1[i] if i < m else inf
            val2 = nums2[j] if j < n else inf
            num.append(min(val1,val2))
            if val1 <= val2:i+=1 
            else:j+=1
        nums1[:]=num