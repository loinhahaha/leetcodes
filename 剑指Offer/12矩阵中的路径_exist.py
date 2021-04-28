# Find exact path in an alphabet matrix
# Tip: Use depth first algorithm.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        def dfs(i, j, k):  # i len(column) j len(row) k len(word)
            if not 0 <= i < M or not 0 <= j < N or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True

            board[i][j] = ''  # avoid repeat
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]  # reset
            return res

        for i in range(M):
            for j in range(N):
                if dfs(i,j,0): return True
        
        return False
      
