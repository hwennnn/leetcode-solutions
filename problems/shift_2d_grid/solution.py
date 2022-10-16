class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        k %= rows * cols
        
        for _ in range(k):
            temp = [[0] * cols for _ in range(rows)]
            
            for i in range(rows):
                if i + 1 < rows:
                    temp[i + 1][0] = grid[i][cols - 1]
                    
                for j in range(cols):
                    if j + 1 < cols:
                        temp[i][j + 1] = grid[i][j]
                
            temp[0][0] = grid[rows - 1][cols - 1]
            
            grid = temp
        
        return grid

    