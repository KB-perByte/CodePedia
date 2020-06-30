#code
def check(arr, k):
        count =0
        arr.sort()  
        l =0
        r=0
        n = len(arr)
        while r<n: 
            if arr[r]-arr[l]==k: 
                count+=1
                l+=1
                r+=1
            elif arr[r]-arr[l]>k:  
                l+=1
            else: 
                r+=1
        return 1 if count > 0 else -1

n = int(input())
while(n):
    n-=1
    par = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    print(check(arr, par[1]))