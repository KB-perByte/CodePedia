for _ in range(int(input())):
    m, n = input().split()
    _mn , _n, final = [], [], None
    for i in range(len(m)):
        diff = ord(m[i])-ord(n[i])
        _n.append(diff)        
        if i > 1:
            if _n[i-1] == diff:
                final = True
                continue
            else:
                print('NO')
                final = False
                break
    if final:
        print('YES')
    