class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        m = 1
        while m<=n:
            a = n/m
            b = n%m
            res += (a+8)/10 * m
            if a%10==1:
                res += b+1
            m *= 10
        return res