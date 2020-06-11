from collections import defaultdict
import bisect 

class Solution:
    def isSubsequence(self, s, t):
        rankDict = defaultdict(list)
        pos = 0

        for i, k in enumerate(t):
            rankDict[k].append(i)
        
        for k in s:
            idx = bisect.bisect_left(rankDict[k], pos)
            if idx >= len(rankDict[k]):
                return False
            pos = rankDict[k][idx] + 1
            
        return True

s = Solution()
print(s.isSubsequence('abc','axdbsec'))


def isSubsequenceOld(s, t):
    ans =""
    for i in s:
        if i in t:
            ans+=i
            t=t[t.index(i)+1:]

    if ans== s:
        return True

print(isSubsequenceOld('abc','axcdbsec'))