class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen_sums = defaultdict(int)
        
        for acc in accumulate(nums, initial=0):
            count += seen_sums[acc - k]
            seen_sums[acc] += 1
        
        return count