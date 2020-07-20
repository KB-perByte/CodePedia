cases = int(input())
for z in range(cases):
    n = int(input())
    arr = list(map(int,input().split()))
    d,minm,flg = {},100001,0
    for i in arr:
        if minm>i:
            minm = i
        if i not in d:
            d[i] = 1
        else:
            flg = 1
    n = len(d)
    #print(d,n)
    for i in range(n):
        if minm not in d:
            flg = 1
            break
        minm += 1
    #print(d)
    if flg == 1:
        print("No")
    else:
        print("Yes")
            