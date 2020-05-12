import math 
T=int(input())
for i in range(T):
    N,K=[int(s) for s in input().split(" ")] 
    session=[int(s) for s in input().split(" ")]
    sess_diff=[session[x+1]-session[x] for x in range(len(session)-1)]
    
    di_max=max(sess_diff)
    ll=1
    rr=di_max
    while ll<rr: 
        mid=int((ll+rr)/2)
        if sum(map(lambda x: math.ceil(x/mid)-1,sess_diff)) <= K:
            rr=mid
        else:
            ll=mid+1 
    ans=ll

    print("Case #{}: {}".format(i+1, ans)) 
