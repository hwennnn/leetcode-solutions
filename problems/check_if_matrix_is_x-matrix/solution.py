class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == j or i + j == cols - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        
        return True