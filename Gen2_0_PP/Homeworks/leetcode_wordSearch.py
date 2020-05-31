class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recur(word, r, c):
            if word[0] != board[r][c]:
                return False
            if len(word) == 1:
                return True
            
            ans = False 
            used.add((r,c))
            if r > 0 and (r-1, c) not in used:
                ans |= recur(word[1:], r-1, c) 
            if c > 0 and (r, c-1) not in used and not ans:
                ans |= recur(word[1:], r, c-1) 
            if r < len(board)-1 and (r+1, c) not in used and not ans:
                ans |= recur(word[1:], r+1, c) 
            if c < len(board[0])-1 and (r, c+1) not in used and not ans:
                ans |= recur(word[1:], r, c+1) 
            used.remove((r, c))
            return ans 
            
        used = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if recur(word, r, c):
                    return True
                
        return False