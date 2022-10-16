class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        if not matrix or rows == 0 or cols == 0: return False
        
        row, col = 0, cols - 1
        
        while row < rows and col >= 0:
            curr = matrix[row][col]
            
            if curr == target: 
                return True
            elif curr > target: 
                col -= 1
            else:
                row += 1
                
        return False