class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        @cache
        def go(x, y):
            count = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and matrix[dx][dy] > matrix[x][y]:
                    count = max(count, 1 + go(dx, dy))
            
            return count
        
        res = 0
        
        for x in range(rows):
            for y in range(cols):
                res = max(res, go(x, y))
        
        return res