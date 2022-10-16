class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        horizontal = [[0] * cols for _ in range(rows)]
        vertical = [[0] * cols for _ in range(rows)]
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    horizontal[i][j] += (1 if j == 0 else 1 + horizontal[i][j - 1])
                    vertical[i][j] += (1 if i == 0 else 1 + vertical[i - 1][j])
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                size = min(horizontal[i][j], vertical[i][j])
                
                while size > res:
                    if horizontal[i - size + 1][j] >= size and vertical[i][j - size + 1] >= size:
                        res = size
                    
                    size -= 1
        
        return res * res