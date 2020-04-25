#Homework Array-1
# n, a = map(int,input().split())
# t = map(int,input().split())
# t = list(t)
# ans = 0
# for i in range(n):
#     if t[i]:
#         d = i - a
#         j = a - d
#         if j < 1 or j > n or t[i] == t[j]:
#             ans += 1
# print(ans)

#----------------------
n, a = map(int,input().split())
v = map(int,input().split())
v = list(v)
ans = 0
for i in range(n):
    if a - i < 1  and a + i > n:
        break
    elif a - i >= 1 and a + i <= n and v[a - i] == v[a + i]:
        ans += 2 * v[a - i]
    elif a - i >= 1 and a + i > n:
        ans += v[a - i]
    elif a - i < 1  and a + i <= n:
        ans += v[a + i]
print(ans)
#----------------------