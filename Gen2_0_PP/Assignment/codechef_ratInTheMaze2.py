def issafe(i,j,a):
    n=len(a)
    if (i>=0 and i<=n-1) and (j>=0 and j<=n-1) and a[i][j]!=0:
         return True
    return False
def fun(a,i,j,temp,n):
    if i==j and j==n-1:
        print("".join(temp),end=' ')
        return
    var=a[i][j]
    a[i][j]=0
    if issafe(i+1,j,a):
        temp.append("D")
        fun(a,i+1,j,temp,n)
        temp.pop()
    if issafe(i,j-1,a):
        temp.append("L")
        fun(a,i,j-1,temp,n)
        temp.pop()
    if issafe(i,j+1,a):
        temp.append("R")
        fun(a,i,j+1,temp,n)
        temp.pop()
    if issafe(i-1,j,a):
        temp.append("U")
        fun(a,i-1,j,temp,n)
        temp.pop()
    a[i][j]=var 
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(arr[i*n:(i+1)*n])
    #rint(a)
    fun(a,0,0,[],n)
    print()
    #rint("asd")