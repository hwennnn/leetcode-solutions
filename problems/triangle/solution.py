class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        
        for i in range(1, rows):
            for j in range(len(triangle[i])):
                first = triangle[i - 1][j] if j < len(triangle[i - 1]) else float('inf')
                second = triangle[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                
                triangle[i][j] += min(first, second)
        
        return min(triangle[-1])