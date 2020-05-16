#!/usr/bin/python3

cost = 0
    
n, s = map(int, input().split())
a = list(map(int, input().split()))

def funcMonotonic(a, s, k):
    global cost
    costs = [a[i] + (i + 1) * k for i in range(n)]
    costs.sort()
    cost = sum(costs[:k])
    return cost <= s

left, right = 0, n + 1
while left + 1 < right:
    middle = (left + right) // 2
    if funcMonotonic(a, s, middle):
        left = middle
    else:
        right = middle

funcMonotonic(a, s, left)
print(left, cost)
