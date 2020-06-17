class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def f(ele):
            if ele in S:
                return S.index(ele)  # As the sorting algorithm is based on the order in which they occur. We can use the index of the character
            return -1
        
        T = list(T)
        S = list(S)
        
        
        T.sort(key=f)
        return ''.join(T)