class Solution:
    def __init__(self):
        self.max_len = 0
        self.table = {}
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        def dfs(x, y, prev):            
            if not (0 <= x < rows and 0 <= y < cols) or matrix[x][y] <= prev: return 0
            
            if (x, y) in self.table: return self.table[(x, y)]
            
            path = float('-inf')
            for dx, dy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                path = max(path, dfs(dx, dy, matrix[x][y]))
            path += 1
            
            self.max_len = max(self.max_len, path)
            self.table[(x, y)] = path
            
            return path
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, float('-inf'))       
        
        return self.max_len