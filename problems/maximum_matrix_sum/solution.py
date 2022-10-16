class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        total = count = 0
        mmin = float('inf')
        
        for i in range(rows):
            for j in range(cols):
                total += abs(matrix[i][j])
                
                if matrix[i][j] < 0: count += 1
                mmin = min(mmin, abs(matrix[i][j]))
        
        if count % 2 == 0:
            return total
        else:
            return total - 2 * mmin
        
        