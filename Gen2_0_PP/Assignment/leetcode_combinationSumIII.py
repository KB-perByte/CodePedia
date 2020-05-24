class Solution:
    def __init__(self):
        self.answer = set()
    def helper(self,k,n,ans=set()):
        if n<0 or k<0: return
        elif n==0 and k==0:
            self.answer.add(tuple(sorted(list(ans))))
            return
        elif n==0 and k>0:
            return
        for i in range(1,10):
            if i not in ans and n>=i and k>0:
                self.helper(k-1,n-i,ans|{i})
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.helper(k,n)
        return self.answer