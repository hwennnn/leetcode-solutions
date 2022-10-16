class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols+1) for _ in range(rows+1)]
        
        for i in range(1, rows+1):
            c = 0
            for j in range(1, cols + 1):
                c += mat[i-1][j-1]
                prefix[i][j] = prefix[i-1][j] + c
        
        for k in range(min(rows,cols)-1, -1, -1):
            for i in range(1, rows - k + 1):
                for j in range(1, cols - k + 1):
                    if prefix[i+k][j+k] - prefix[i-1][j+k] - prefix[i+k][j-1] + prefix[i-1][j-1] <= threshold:
                        return k+1;

        return 0