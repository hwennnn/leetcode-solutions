class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        
        def backtrack(x, y, i, curr, visited):
            if curr == word:
                return True
            
            for dx,dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and board[dx][dy] == word[i] and (dx, dy) not in visited:
                    visited.add((dx, dy))
                    result = backtrack(dx, dy, i + 1, curr + board[dx][dy], visited)
                    visited.remove((dx, dy))
                    
                    if result: return True
            
            return False
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == word[0]:
                    if backtrack(x, y, 1, word[0], set([(x, y)])):
                        return True
            
        return False