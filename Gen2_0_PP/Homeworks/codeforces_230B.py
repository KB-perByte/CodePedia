import sys
N = 10**6 + 1
f = sys.stdin
_ = int(f.readline())
inp = [int(i) for i in f.readline().strip().split()]
steveArr = [True] * N
_steBool = set()
for i in range(2, N):
    if steveArr[i]:
        _steBool.add(i**2)
        for j in range(i, N, i):
            steveArr[j] = False

for i in inp:
    if i in _steBool:
        print("YES")
    else:
        print("NO")