from collections import Counter
t = int(input())
while(t):
    t-=1
    lst = list(map(int,input().split()))
    _v = Counter(lst)
    cnt = 0
    for k,v in dict(_v).items():
        if v > k :
            cnt+=(v-k)
    print(cnt)
        
