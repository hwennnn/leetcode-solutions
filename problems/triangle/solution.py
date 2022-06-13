class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        for i in range(1, n):
            for j in range(len(triangle[i])):
                l = triangle[i - 1][j - 1] if j - 1 >= 0 else float('inf')
                r = triangle[i - 1][j] if j < len(triangle[i - 1]) else float('inf')
                triangle[i][j] += min(l, r)
        
        return min(triangle[-1])