class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        if not triangle: return 0
        if n == 1: return triangle[0][0]
        
        for i in range(1,n):
            row = triangle[i]
            
            for j in range(len(row)):
                if j == 0:
                    row[j] += triangle[i-1][j]
                
                elif j == len(row)-1:
                    row[j] += triangle[i-1][j-1]
                
                else:
                    row[j] += min(triangle[i-1][j], triangle[i-1][j-1])
                
        
        return min(triangle[-1])
            