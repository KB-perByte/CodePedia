#code
t=int(input())
for f in range(t):
    n=int(input())
    l=input().split()
    for i in range(n):
        l[i]=int(l[i])
   
    for i in range(n):
        
        if l[abs(l[i])-1]>0:
            l[abs(l[i])-1]=-l[abs(l[i])-1]
        else:
            x=abs(l[i])
            print(x,end=' ')
            break
        
    s=0
    for i in range(n):
        s=s+abs(l[i])
    s=s-x
    print(((n*(n+1))//2)-s)
    
        

t=int(input())
for _ in range(t):
    n=int(input())
    arr=input().split()
    check=[0]*len(arr)
    for i in range(len(arr)):
        if( not check[int(arr[i])-1]):
            check[int(arr[i])-1]=1
        else:
            print(int(arr[i]), end=" ")
    for i in range(len(check)):
        if(not check[i]):
            print(i+1)