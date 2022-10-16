class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.res = 1
        
        rowPrefix = [[i for i in row] for row in grid]
        colPrefix = [[i for i in row] for row in grid]
        dlPrefix = [[i for i in row] for row in grid]
        drPrefix = [[i for i in row] for row in grid]
        
        # row
        for i in range(rows):
            for j in range(cols - 1):
                rowPrefix[i][j + 1] += rowPrefix[i][j]

        # cols
        for i in range(rows - 1):
            for j in range(cols):
                colPrefix[i + 1][j] += colPrefix[i][j]

        # diag left
        for i in range(rows - 1):
            for j in range(cols - 1):
                dlPrefix[i + 1][j + 1] += dlPrefix[i][j]

        # diag right
        for i in range(rows - 1):
            for j in range(cols - 1, 0, -1):
                drPrefix[i + 1][j - 1] += drPrefix[i][j]

        def dfs(x, y, size):
            
            if x + size < rows and y + size < cols:
                rowSum = [rowPrefix[i][y + size] - (0 if y == 0 else rowPrefix[i][y - 1]) for i in range(x, x + size + 1)]
                colSum = [colPrefix[x + size][j] - (0 if x == 0 else colPrefix[x - 1][j]) for j in range(y, y + size + 1)]
                diagLeft = dlPrefix[x + size][y + size] - (0 if x == 0 or y == 0 else dlPrefix[x - 1][y - 1])
                diagRight = drPrefix[x + size][y] - (0 if x - 1 < 0 or y + size + 1 >= cols else drPrefix[x - 1][y + size + 1])
                
                if (all(r == rowSum[0] for r in rowSum) and all(c == colSum[0] for c in colSum) and rowSum[0] == colSum[0] == diagLeft == diagRight):
                    self.res = max(self.res, size + 1)
                    
                dfs(x, y, size + 1)
            
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 1)
        
        return self.res