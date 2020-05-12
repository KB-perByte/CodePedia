
import sys

n, x = (map (int, sys.stdin.readline ().strip ().split (' ')))
a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

k=0

for i in range(0,n,+1):
    print(i)
    subArraySum=[]
    for j in range (0, n-i, +1):
        subArraySum.append (sum(a[j:j+i+1]))

    if(max(subArraySum)<=x):
        k+=1

print(k)
