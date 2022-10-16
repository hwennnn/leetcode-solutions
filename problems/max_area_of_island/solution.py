class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def go(x, y):
            res = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    grid[dx][dy] = 0
                    res += go(dx, dy)
            
            return res
        
        ans = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    ans = max(ans, go(i, j))
        
        return ans