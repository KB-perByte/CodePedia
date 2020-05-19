def findval(s_arr,rank):
    l,r=0,n-1
    while(l<=r):
        m=l+(r-l)//2
        if s_arr[m]>=rank and s_arr[m-1]<rank and m!=0:
            return [m,rank-s_arr[m-1]]
        elif m==0:
            if s_arr[m]>=rank:
                return [m,rank]
            else:
                return -1
        else:
            if s_arr[m-1]>=rank and s_arr[m]>rank and m!=0:
                r=m-1
            elif s_arr[m]<rank:
                l=m+1
    return -1
                
inp=list(map(int,input().split()))
n,m=inp[0],inp[1]
arr=list(map(int,input().split()))
queries=list(map(int,input().split()))

prefixArr=[0]*n
prefixArr[0]=arr[0]
if len(arr)==0:
    print(0)
for i in range(1,n):
    prefixArr[i]=prefixArr[i-1]+arr[i]

for i in range(m):
    ans=findval(prefixArr,queries[i])
    if ans==(-1):
        print(None)
    else:
        print(ans[0]+1,ans[1])
    
