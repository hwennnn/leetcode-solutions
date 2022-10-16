class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        matrix.reverse()
        
        for i in range(rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]