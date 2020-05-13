class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        lowest = max(sum(weights)//D, max(weights)); highest = sum(weights)//D
        def count(capacity, D):
            cur_sum, cnt = 0, 0
            for w in weights:   
                if cur_sum+w > capacity:
                    cnt+=1
                    cur_sum = 0
                cur_sum+=w
            return cnt+1<=D

        l, r = lowest, highest
        while l<r:
            mid = l+(r-l)//2
            if count(mid, D):
                r = mid
            else:
                l = mid+1
        return r

class Solution2:     
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = left * len(weights) // D
        
        while left <= right:
            mid = (left + right) // 2
            if not self.is_possible(mid, weights, D):
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def is_possible(self, capacity, weights, days_count):
        
        remain = capacity
        count = 1
        for w in weights:
            if w > remain:
                count += 1
                remain = capacity
                
            remain -= w
        return count <= days_count
