class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + mat[i][j]

        for i in range(rows):
            for j in range(cols):
                r1, r2 = max(0, i - k), min(rows, i + k + 1)
                c1, c2 = max(0, j - k), min(cols, j + k + 1)
                
                mat[i][j] = (prefix[r2][c2] - prefix[r1][c2]) - (prefix[r2][c1] - prefix[r1][c1])
        
        return mat
        
    