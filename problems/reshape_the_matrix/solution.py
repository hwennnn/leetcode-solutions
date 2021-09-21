class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c: return mat
        
        res = [[0] * c for _ in range(r)]
        
        for i in range(rows * cols):
            res[i // c][i % c] = mat[i // cols][i % cols]
        
        return res