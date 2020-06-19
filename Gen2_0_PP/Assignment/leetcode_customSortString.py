class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def compFunc(ele):
            if e in S:
                return S.index(e)
            return -1
        
        T,S = list(T), list(S)
        T.sort(key=compFunc)
        return ''.join(T)