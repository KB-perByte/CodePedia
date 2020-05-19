def checkConsonat(ch):
    if( ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return False
    else:
        return True

# res = ''

# def func(st, pos, res = ''):
#     if checkConsonat(st[pos]):
#         func(st , pos, res+' '+st[pos])
#         func(st , pos, res+st[pos])
#     res

n = int(input())
st = str(input())
dec = 0

def proc(st, dec):
    #dec = 0
    while dec <= len(st):
        ans = ''
        for i in st:
            if checkConsonat(i):
                ans+=' '
                ans+=i
            else:
                ans+=i
        print(ans)
        dec+=1
        return proc(st[:dec], dec)

print(proc(st, dec))


'''
BAC
B
'''
