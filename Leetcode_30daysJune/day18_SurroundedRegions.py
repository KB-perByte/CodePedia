class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            if i == 0 or i == m - 1:
                for j in range(n):
                    self.dfs(board, i, j)
            else:
                self.dfs(board, i, 0)
                self.dfs(board, i, n - 1)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = "X" if board[i][j] != "M" else "O"
            
    def dfs(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
            return
        
        board[i][j] = "M"
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)