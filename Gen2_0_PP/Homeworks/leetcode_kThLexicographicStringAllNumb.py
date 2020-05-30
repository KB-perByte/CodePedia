import math
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3*2**(n-1)
        if total < k : return ""
        res = ""
        if k <= 2**(n-1):
            l = 0
            h = 2**(n-1)
            res +="a"
        elif k <= 2**n:
            l = 2**(n-1)
            h = 2**n
            res +="b"
        else:
            l = 2**(n)
            h = 3*2**(n-1)
            res +="c"
        prev = res

        s = []
        for i in range(n-1):
            mid = l + (h-l)//2

            if mid < k:
                s.append(1)
                l = mid
            else:
                s.append(0)
                h = mid
  
        for i in s:
            ch =["a","b","c"]
            ch.remove(prev)

            res+=ch[int(i)]
            prev = ch[int(i)]
        print(res)    
        return res    