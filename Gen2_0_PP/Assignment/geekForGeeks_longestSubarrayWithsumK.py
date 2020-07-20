#code
def largest(arr,n,k):
    sum=0
    count=0
    mydict={}
    for i in range(n):
        sum+=arr[i]
        if(sum==k):
            count=i+1
        elif(sum-k in mydict):
            count=max(count,i-mydict[sum-k])
        if sum not in mydict:
            mydict[sum]=i
    return count
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    res=largest(l,n,k)
    print(res)