class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def countPerimeter(x, y):
            top = 1 if y == 0 or (y - 1 >= 0 and grid[x][y - 1]) == 0 else 0
            left = 1 if x == 0 or (x - 1 >= 0 and grid[x - 1][y] == 0) else 0
            right = 1 if x == rows - 1 or (x + 1 < rows and grid[x + 1][y] == 0) else 0
            bottom = 1 if y == cols - 1 or (y + 1 < cols and grid[x][y + 1] == 0) else 0

            return top + left + right + bottom
        
        def dfs(x, y):
            count = countPerimeter(x, y)
            grid[x][y] = -1
            
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    count += dfs(dx, dy)
            
            return count
        
        res = float('-inf')
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res