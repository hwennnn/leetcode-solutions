class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        R = []
        C = []
        
        def countDivisor(x):
            a = b = 0
            
            while x % 2 == 0:
                x //= 2
                a += 1
            
            while x % 5 == 0:
                x //= 5
                b += 1
            
            return (a, b)
        
        for x in range(rows):
            curr = [(0, 0)]
            for y in grid[x]:
                a, b = countDivisor(y)
                curr.append((curr[-1][0] + a, curr[-1][1] + b))
                
            R.append(curr)
        
        for y in range(cols):
            curr = [(0, 0)]
            for x in range(rows):
                a, b = countDivisor(grid[x][y])
                curr.append((curr[-1][0] + a, curr[-1][1] + b))
            
            C.append(curr)

        res = 0
        
        for x in range(rows):
            for y in range(cols):
                topLeft = min(R[x][y + 1][0] + C[y][x][0], R[x][y + 1][1] + C[y][x][1])
                topRight = min(R[x][-1][0] - R[x][y][0] + C[y][x][0], R[x][-1][1] - R[x][y][1] + C[y][x][1])
                botLeft = min(R[x][y][0] + C[y][-1][0] - C[y][x][0], R[x][y][1] + C[y][-1][1] - C[y][x][1])
                botRight = min(R[x][-1][0] - R[x][y + 1][0] + C[y][-1][0] - C[y][x][0], R[x][-1][1] - R[x][y + 1][1] + C[y][-1][1] - C[y][x][1])
                res = max(res, topLeft, topRight, botLeft, botRight)

        return res