class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(1, rows):
            for j in range(cols):
                left = float('inf') if j == 0 else matrix[i - 1][j - 1]
                mid = matrix[i - 1][j]
                right = float('inf') if j == cols - 1 else matrix[i - 1][j + 1]
                matrix[i][j] += min(left, mid, right)
        
        return min(matrix[-1])