
def recFunc(current,cNext,r,c):
    if(current==r-1 and cNext==c-1):
        return 1
    elif(current==r-1):
        return recFunc(current,cNext+1,r,c)
    elif(cNext==c-1):
        return recFunc(current+1,cNext,r,c)
    else:
        return recFunc(current+1,cNext,r,c) + recFunc(current,cNext+1,r,c)
    
n=int(input())

for i in range(n):
    r,c = map(int,input().split(' '))
    paths = recFunc(0,0,r,c)
    print(paths)