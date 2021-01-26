class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        def good(k):
            visited = set()
            
            def dfs(x, y):
                if x == rows - 1 and y == cols - 1: return True
                
                if 0 <= x < rows and 0 <= y < cols:
                    for dx,dy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        if 0 <= dx < rows and 0 <= dy < cols and (dx,dy) not in visited and abs(heights[x][y] - heights[dx][dy]) <= k:
                            visited.add((dx,dy))
                            if dfs(dx,dy): 
                                return True
                    
                return False
            
            return dfs(0,0)
                            
            
        
        left, right = 0, 1000000
        
        while left < right:
            mid = left + (right-left) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
            
        return left