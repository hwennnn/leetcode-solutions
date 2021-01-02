class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i,j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] != 1:
                grid[i][j] = 1
                
                dfs(i, j-1)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i+1, j)

                
        res = 0
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dfs(i,j)
                    res += 1
        
        
        return res