#code
M = 1000000007
testCases = int(input())
for i in range(testCases):
    N = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    for i in range(0, N):
        sum += (arr[i] * (i+1) * (N-i))
    print(sum%M)