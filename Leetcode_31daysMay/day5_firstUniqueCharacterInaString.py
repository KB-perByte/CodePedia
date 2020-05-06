class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = collections.Counter(s)
        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i    
        return -1