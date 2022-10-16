class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        res = 0
        A = [[0] * (n * 3) for _ in range(n * 3)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    A[i * 3][j * 3 + 2] = A[i * 3 + 1][j * 3 + 1] = A[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == "\\":
                    A[i * 3][j * 3] = A[i * 3 + 1][j * 3 + 1] = A[i * 3 + 2][j * 3 + 2] = 1
                    
        def dfs(x, y):
            A[x][y] = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < n * 3 and 0 <= dy < n * 3 and A[dx][dy] == 0:
                    dfs(dx, dy)
        
        for x in range(n * 3):
            for y in range(n * 3):
                if A[x][y] == 0:
                    dfs(x, y)
                    res += 1
        
        return res