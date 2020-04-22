#Homework Array-1
n, a = map(int,input().split())
t = map(int,input().split())
t = list(t)
ans = 0
for i in range(n):
    if t[i]:
        d = i - a
        j = a - d
        if j < 1 or j > n or t[i] == t[j]:
            ans += 1
print(ans)
