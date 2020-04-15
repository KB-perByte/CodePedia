noOfInput = int(input())
for inp in range(noOfInput):
    N = int(input())
    A = list(map(int, input().split()))
    prev = -10
    flag = 1
    for i in range(N):

        if (A[i]==1):
            if ((i-prev) < 6):
                flag = 0
                break
            prev = i
    if (flag == 1):
        print("YES")
    else:
        print("NO")