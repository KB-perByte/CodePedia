
ans = float('inf')

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x / y,
      '*': lambda x, y: x * y}

def rec_3(a, b):
    global ans
    temp=0
    temp = op[st[2]](a,b) if( st[2]=='+') else op['*'](a,b)
    ans=min(ans,temp)

def rec_2(a, b, c):

    if( st[1]=='+'):
        rec_3(a+b,c)
        rec_3(a+c,b)
        rec_3(b+c,a)
    
    else:    
        rec_3(a*b,c)
        rec_3(a*c,b)
        rec_3(b*c,a)
    
def rec_1( a, b, c, d):
    if( st[0]=='+'):
        rec_2(a+b,c,d)
        rec_2(a+c,b,d)
        rec_2(a+d,b,c)
        rec_2(b+c,a,d)
        rec_2(b+d,a,c)
        rec_2(c+d,a,b)
    
    else:
        rec_2(a*b,c,d)
        rec_2(a*c,b,d)
        rec_2(a*d,b,c)
        rec_2(b*c,a,d)
        rec_2(b*d,a,c)
        rec_2(c*d,a,b)


nom = list(map(int,input().split()))
st = list(map(str,input().split()))
rec_1(nom[0],nom[1],nom[2],nom[3])
print(ans)