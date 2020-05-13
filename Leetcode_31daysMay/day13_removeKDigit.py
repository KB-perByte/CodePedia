class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n, j = list(num), k
        arr = []
        for _ in range(len(num)-k):
    	    i = n.index(min(n[:j+1]))
    	    arr.append(n[i])
    	    j -= i
    	    del n[:i+1]
        return "".join(arr).lstrip("0") or "0"
		
		