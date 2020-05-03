from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        _mags = Counter(magazine)
        _rans = Counter(ransomNote)
        
        for c in _rans:
            if c not in _mags or _mags[c] < _rans[c]:
                return False
            
        return True