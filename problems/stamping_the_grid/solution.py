class Solution:
    def possibleToStamp(self, grid: List[List[int]], H: int, W: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + grid[i][j]
        
        diff = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows - H + 1):
            for j in range(cols - W + 1):
                count = prefix[i + H][j + W] - prefix[i][j + W] - prefix[i + H][j] + prefix[i][j]
                
                if count == 0:
                    diff[i][j] += 1
                    diff[i][j + W] -= 1
                    diff[i + H][j] -= 1
                    diff[i + H][j + W] += 1
        
        for i in range(rows + 1):
            for j in range(cols):
                diff[i][j + 1] += diff[i][j]
        
        for j in range(cols + 1):
            for i in range(rows):
                diff[i + 1][j] += diff[i][j]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and diff[i][j] == 0:
                    return False
        
        return True