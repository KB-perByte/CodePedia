n = int(input())
ans = 0
while(n):
    if(n==1):
        ans=1
    elif(n==2):
        ans=2
    elif(n==3):
        ans=6
    elif(n%2==0):
        if(n%3==0):
            ans=(n-1)*(n-2)*(n-3)
        else:
            ans=n*(n-1)*(n-3)
    else:
        ans=n*(n-1)*(n-2)
    print(ans)
    break
    
