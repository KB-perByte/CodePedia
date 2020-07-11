class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height)-1
        maxi = 0
        while(low < high):
            maxi = max(maxi, (high - low)*min(height[low], height[high]))
            if height[low] < height[high]:
                low+=1
            else: high-=1
        return maxi