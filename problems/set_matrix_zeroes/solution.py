class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        setCol0 = False
        
        for x in range(rows):
            setCol0 |= matrix[x][0] == 0
            for y in range(1, cols):
                if matrix[x][y] == 0:
                    matrix[x][0] = matrix[0][y] = 0
        
        for x in range(rows - 1, -1, -1):
            for y in range(1, cols):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0
            
            if setCol0: 
                matrix[x][0] = 0