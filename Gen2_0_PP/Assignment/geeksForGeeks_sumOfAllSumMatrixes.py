M = 1000000007
arr = []
sum = 0
testCases = int(input())
for i in range(testCases):
    N = int(input())
    for x in range(N):
        arr.append(
            list(map(int,input().split()))
            )

    n = N
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            sum+=arr[i][j]*(i+1)*(j+1)*(n-i)*(m-j)
        
    print(sum%M)
