class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res,codeset = set(), set()           
        charmap = {"A":0,"C":1,"G":2,"T":3}
        for i in xrange(0,len(s)-9):
            code = 0
            for j in xrange(i,i+10):
                code <<= 2
                code |= charmap[s[j]]
            
            if code in codeset:
                res.add(s[i:i+10])
            else:
                codeset.add(code)                
        return list(res)
ss = Solution()
ss.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')