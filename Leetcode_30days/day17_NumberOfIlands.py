class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'

        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)