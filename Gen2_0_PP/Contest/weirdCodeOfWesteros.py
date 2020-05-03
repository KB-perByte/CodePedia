# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
res=0
a=int(raw_input())
for i in range(a):
    x,y=raw_input().strip().split(" ")
    a,b=int(x),int(y)
    L=int(math.sqrt(a))
    R=int(math.sqrt(b))
    for j in range(L,R+1):
        cnt=0
        for k in range(1,j+1):
            if (j%k==0):
                cnt=cnt+1
        if cnt==2:
            res=res+1
    print(res) 