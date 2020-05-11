def minSwap(arr, n, k) : 
    count = 0
    for i in range(0, n) : 
        if (arr[i] <= k) : 
            count = count + 1

    x = 0
    for i in range(0, count) : 
        if (arr[i] > k) : 
            x = x + 1
    ans = x 
    j = count 
    for i in range(0, n) : 
        if(j == n) : 
            break
        if (arr[i] > k) : 
            x = x - 1
        if (arr[j] > k) : 
            x = x + 1
        ans = min(ans, x) 
        j = j + 1
    return ans 

for i in range(int(input())):
    n = int(input())
    arr = []
    arr = list(map(int,input().split()))
    k = int(input())
    minSwap(arr, n, k)
#try:
#minSwap([2,1,5,6,3], 5, 5)
#except:
#   pass