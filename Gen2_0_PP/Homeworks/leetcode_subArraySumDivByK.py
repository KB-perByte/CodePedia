class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans,psum,mymap = 0,0,{}
        for num in A:
            mymap[psum] = mymap.get(psum,0) + 1
            psum += num
            psum %= K
            if mymap.get(psum%K):
                ans += mymap.get(psum%K)
        print(mymap)
        return ans
    