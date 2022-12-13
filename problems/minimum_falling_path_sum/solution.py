class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(1, rows):
            for j in range(cols):
                left = matrix[i - 1][j - 1] if j - 1 >= 0 else inf
                mid = matrix[i - 1][j]
                right = matrix[i - 1][j + 1] if j + 1 < cols else inf

                matrix[i][j] += min(left, mid, right)

        return min(matrix[-1])