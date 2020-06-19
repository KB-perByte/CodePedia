

for _ in range(int(input().strip())):
    
    n = int(input().strip())
    ar = list(map(int, input().strip().split()))
    
    sar = sorted(ar)
    
    s = 0
    
    while (ar[s] == sar[s]):
        s += 1
        if (s == n):
            s= n-1
            break
        
    e = n-1
    while (ar[e] == sar[e]):
        e -= 1
        if (e == -1):
            e = 0
            break
        
    print (s, e)