class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c: return mat
        
        res = [[0] * c for _ in range(r)]
        ii = jj = 0
        
        for i in range(rows):
            for j in range(cols):
                if jj == c:
                    ii += 1
                    jj = 0
                
                res[ii][jj] = mat[i][j]
                jj += 1
        
        return res