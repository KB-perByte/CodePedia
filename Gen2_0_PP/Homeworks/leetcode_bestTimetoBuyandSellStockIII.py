class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 1:
            return 0
        l, r = [0] * n, [0] * n
        l_min, r_max = prices[0], prices[n-1]
        for i in range(1, n):
            if prices[i] < l_min:
                l_min = prices[i]
            l[i] = max(l[i-1], prices[i] - l_min)
         
        for i in range(n-2, -1, -1):
            if prices[i] > r_max:
                r_max = prices[i]
            r[i] = max(r[i+1], r_max - prices[i])
        result = 0
        for i in range(n-1):
            result = max(result, l[i] + r[i])
        return result