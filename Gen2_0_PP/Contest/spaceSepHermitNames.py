
def checkConsonat(ch):
    if( ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return False
    else:
        return True

n = int(input())
st = str(input())
cntConso = 0
visited = 0
a = ''

for i in range(n):
    if checkConsonat(st[i]):
        cntConso += 1
        a+=' '
    a+=st[i]

print(st) #print 1st

for w in range(cntConso):
    _ans = ''
    for i in range(visited, n):
        if checkConsonat(st[i]):
            _ans += st[:i]
            visited = i+1
            _ans+=' '
            _ans += st[i:]
            print(_ans)
            _ans = ''
            i = n
    #print(_ans)

print(a) #print last