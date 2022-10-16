class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        
        top = 0
        bottom = rows - 1
        
        while bottom > top:
            mid = (top + bottom) // 2
            if max(mat[mid]) > max(mat[mid+1]):
                bottom = mid
            else:
                top = mid + 1
                
        return [bottom, mat[bottom].index(max(mat[bottom]))]