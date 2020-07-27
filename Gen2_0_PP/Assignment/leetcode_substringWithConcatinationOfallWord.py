class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(s) == 0: return []
        if len(s) < len(''.join(words)): return []
        
        rst = []
        words_cat = ''.join(sorted(words))
        l, m = len(words[0]), len(words)
        l_all = len(words_cat)
        
        for i in range(len(s) - l_all + 1): 
            s_sub = []
            for j in range(m):
                s_sub.append(s[i + l * j : i + l * (j+1)])       
            s_sub = ''.join(sorted(s_sub))
            if s_sub == words_cat: rst.append(i)
        
        return rst 