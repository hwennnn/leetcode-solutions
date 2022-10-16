class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            r, c = divmod(mid, cols)
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False