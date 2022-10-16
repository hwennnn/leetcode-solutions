class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        for row in map(sorted, matrix):
            for j, col in enumerate(row):
                res = max(res, col * (cols - j))
        
        return res
            