n,s = map(int, input().split())
a = list(map(int,input().split()))
wsum=0
start=0
flag=0
for i in range(n):
    if flag==0:
        wsum=wsum+a[i]
        while wsum>s:
            wsum=wsum-a[start]
            start=start+1
        if wsum==s:
            flag=1
            print(start+1,end=" ")
            print(i+1, )
        
if flag==0:
    print('-1')

        
        