'''
N = int(input())  
arr = list(map(int,input().split()))
arr.sort()
visible = 1
for i in range(1, N):
    if arr[i] == arr[i-1]:
        visible +=1
print(visible)
'''

from collections import defaultdict
n=int(input())
arr=list(map(int,input().split()))
dic=defaultdict(int)
for i in arr:
    dic[i]+=1
a=list(dic.keys())
a.sort()
vs=n
prev=dic[a[0]]
for i in a[1:]:
    vs-=min(prev,dic[i])
    prev=max(prev,dic[i])
print(vs)