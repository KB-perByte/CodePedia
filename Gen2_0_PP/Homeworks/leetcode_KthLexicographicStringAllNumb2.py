def myStringCreator(s, n, k, myStr):
    if len(myStr)>=k: return 
    if n==0:
        myStr.append(s)
    else:
        if s[-1]=='a':
            myStringCreator(s+'b', n-1, k, myStr)
            myStringCreator(s+'c', n-1, k, myStr)
        elif s[-1]=='b':
            myStringCreator(s+'a', n-1, k, myStr)
            myStringCreator(s+'c', n-1, k, myStr)
        elif s[-1]=='c':
            myStringCreator(s+'a', n-1, k, myStr)
            myStringCreator(s+'b', n-1, k, myStr)


class Solution:
    def getHappymyString(self, n: int, k: int) -> str:
        myStr = []

        myStringCreator('a', n-1, k, myStr)
        myStringCreator('b', n-1, k, myStr)
        myStringCreator('c', n-1, k, myStr)
        print(myStr)
        if k>len(myStr): return ""
        return myStr[k-1]

sl = Solution()
print(sl.getHappymyString(3, 5))