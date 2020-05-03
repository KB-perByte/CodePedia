'''https://www.hackerrank.com/contests/genesis-2-0-self-evaluation-1/challenges'''

for _ in range(int(input())):
    m, n = input().split()
    _n = []
    lnM = len(m)
    lnN = len(n)
    
    for i in range(lnM):
        diff = ((ord(m[i])-ord(n[i])) +26 ) % 26
        _n.append(diff)
    
    if len(set(_n)) > 1:
        print('NO')
    else:
        print('YES')