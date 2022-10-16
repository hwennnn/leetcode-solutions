class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        for i in range(rows - 2):
            for j in range(1, cols - 1):
                res = max(res, grid[i][j - 1] + grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 2][j - 1] + grid[i + 2][j] + grid[i + 2][j + 1])            
        
        return res