import math 
T=int(input())
for i in range(T):
    N,K=[int(s) for s in input().split(" ")] 
    sesn=[int(s) for s in input().split(" ")]
    sess_diff=[sesn[x+1]-sesn[x] for x in range(len(sesn)-1)]
    
    maxDiff=max(sess_diff)
    low=1
    high=maxDiff
    while low<high: 
        mid=int((low+high)/2)
        if sum(map(lambda x: math.ceil(x/mid)-1,sess_diff)) <= K:
            high=mid
        else:
            low=mid+1 
    ans=low

    print("Case #{}: {}".format(i+1, ans)) 
