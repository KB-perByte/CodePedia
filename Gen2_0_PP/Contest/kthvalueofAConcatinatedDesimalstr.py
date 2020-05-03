def getKth(_str, i): 
    ans = str(_str) 
    return ans[i-1]

def findNum(N): 
    total = 0
    once = 9
    dist = 0
    for len in range(1,N): 
        total += once*len
        dist += once 
        if (total >= N): 
            total -= once*len
            dist -= once 
            N -= total
            break         
        once *= 10
    _N = (N / len) 
    d = N % len
    if (d == 0): 
        d = len
    return getKth(dist + _N, d)

for i in range(int(input())):
    print(findNum(int(input())))
