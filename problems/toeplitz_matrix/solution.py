class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        for j in range(cols):
            curr = matrix[0][j]
            ki, kj = 1, j + 1
            
            while ki < rows and kj < cols:
                if matrix[ki][kj] != curr:
                    return False
                
                ki += 1
                kj += 1
        
        for i in range(rows):
            curr = matrix[i][0]                      
            ki, kj = i + 1, 1
            
            while ki < rows and kj < cols:
                if matrix[ki][kj] != curr:
                    return False
                
                ki += 1
                kj += 1
        
        return True
                
            