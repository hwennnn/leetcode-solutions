class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        N = len(word)
        visited = [[False] * cols for _ in range(rows)]

        def go(x, y, index):
            if index == N: return True

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and not visited[dx][dy] and board[dx][dy] == word[index]:
                    visited[dx][dy] = True
                    if go(dx, dy, index + 1): return True
                    visited[dx][dy] = False

            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if go(i, j, 1): return True
                    visited[i][j] = False
        
        return False