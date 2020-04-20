class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        if n<=1:
            return 0
        mp=0
        low=prices[0]
        for i in range(1,n):
            low=min(low,prices[i])
            mp=max(mp, prices[i]-low)
        return mp