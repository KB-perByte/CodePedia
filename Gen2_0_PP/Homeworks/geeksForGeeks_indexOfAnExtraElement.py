def findExtra(a,b,n):
    idx = n 
    l = 0
    r = n - 1
    while (l <= r) : 
        mid = (int)((l + r) / 2) 
        if (b[mid] == a[mid]) : 
            l = mid + 1
        else : 
            idx = mid 
            r = mid - 1
    return idx 
        
#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(findExtra(a,b,n))
# } Driver Code Ends