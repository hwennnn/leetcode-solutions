class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != c * r: return mat
        
        res = [[0] * c for _ in range(r)]
        index = 0
        
        for i in range(rows):
            for j in range(cols):
                res[index // c][index % c] = mat[i][j]
                index += 1
        
        return res