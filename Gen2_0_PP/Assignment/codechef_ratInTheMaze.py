# cook your dish here
solArr = []
flag = False
def solveMaze(i, j):
    global arr, solArr, n, flag, visited

    if (i == n - 1) and (j == n - 1):
        if flag:
            print(' ', end = '')
        else:
            flag = True
        print(''.join(solArr), end = '')

        return

    if i < 0 or i >= n or j < 0 or j >= n or arr[i][j] == 0 or visited[i][j] == 1:
        return

    visited[i][j] = 1

    for c in 'DLRU':
        p, q = i, j
        if c == 'D':
            p = i + 1
        elif c == 'L':
            q = j - 1
        elif c == 'R':
            q = j + 1
        else:
            p = i - 1

        solArr.append(c)
        solveMaze(p, q)
        solArr.pop()

    visited[i][j] = 0
    return

testCase = int(input())
for t in range(testCase):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [[arr[i * n + j] for j in range(n)] for i in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    solArr = []
    flag = False
    solveMaze(0, 0)
    print()