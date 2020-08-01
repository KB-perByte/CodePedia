class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = {0: [], len(s): []}
		#values contain arrays of indices of all words that end at key index
        for ind, c in enumerate(s):
            if not ind in d: #we considered all indices before ind so skipping
                continue
            for w in wordDict:
                if s.startswith(w, ind):
                    ind1 = ind + len(w)
                    ar1 = d.get(ind1, [])
                    if not ar1:
                        d[ind1] = ar1
                    ar1.append(ind)
        d1 = {0: [], len(s) : []}
		#Reconstruct all possible combinations back to index 0
        for ind in range(len(s), 0, -1):
            if not ind in d1:
                continue
            res = d1.get(ind, [])
            for i in d[ind]:
                res1 = [s[i: ind] + ' ' + ns for ns in res] if res else [s[i: ind]]
                res2 = d1.get(i, [])
                if not res2:
                    d1[i] = res1
                else:
                    res2.extend(res1)
        return d1[0]