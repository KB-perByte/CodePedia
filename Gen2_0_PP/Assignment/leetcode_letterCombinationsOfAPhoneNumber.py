class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def helper(pref,i):
            if len(pref) == len(digits):
                res.append(pref)
                return
            
            for j in lookup[digits[i]]:
                pref += j
                helper(pref,i+1)
                pref = pref[:-1]
            
            return
        
        lookup = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
        
        if digits is None or digits == "":
            return []
        
        res = []
        helper("",0)   
        
        return res
        