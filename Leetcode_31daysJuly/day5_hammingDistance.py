class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res=0
        for i in range(32):
            if x&1!=y&1:res+=1
            x=x>>1
            y=y>>1
        return res