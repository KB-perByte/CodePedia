def isPalindrome(self,s):
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def partitionUtil(self,ind,s,stack,res):
    
    if ind >= len(s):
        res.append(list(stack))
        return
    
    for i in range(ind,len(s)):
        if self.isPalindrome(s[ind:i+1]):
            stack.append(s[ind:i+1])
            self.partitionUtil(i+1,s,stack,res)
            stack.pop()

def partition(self, s: str) -> List[List[str]]:
    res = []
    stack = []
    self.partitionUtil(0,s,stack,res)
    return res