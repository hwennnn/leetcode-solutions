class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = [[False] * cols for _ in range(rows)]
        
        def go(x, y):
            if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                self.metBoundary = True
            
            count = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1 and not visited[dx][dy]:
                    visited[dx][dy] = True
                    count += go(dx, dy)
                    
            return count
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and not visited[x][y]:
                    self.metBoundary = False
                    visited[x][y] = True
                    size = go(x, y)
                    
                    if not self.metBoundary:
                        res += size
        
        return res