class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        res = 0
        
        for i in range(rows):
            res += mat[i][i] + mat[i][-i-1]
        
        if rows & 1:
            res -= mat[rows // 2][rows // 2]
                
        return res