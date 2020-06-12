#code
def maze_solve(i, j, n, sol, mat):
    if i == n - 1 and j == n - 1:
        sol[i][j] = 1
        return True
    
    if i >= 0 and i < n and j >= 0 and j < n and mat[i][j]>=1:
        for step in range(1, mat[i][j] + 1):
            if maze_solve(i, j + step, n, sol, mat):
                sol[i][j] = 1
                return True

            if maze_solve(i + step, j, n, sol, mat):
                sol[i][j] = 1
                return True
        
        sol[i][j] = 0
        return False
    else:
        return False
            

for _ in range(int(input())):
    n =int(input())
    mat = [list(map(int, input().split())) for i in range(n)]
    
    sol = [[0 for j in range(n)] for i in range(n)]
    
    if maze_solve(0, 0, n, sol, mat):
        for ele in sol:
            print(*ele)
    else:
        print(-1)