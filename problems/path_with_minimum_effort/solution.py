class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        def good(k):
            queue = collections.deque([(0, 0)])
            visited = set([(0, 0)])
            
            while queue:
                x, y = queue.popleft()
                
                if x == rows - 1 and y == cols - 1:
                    return True
                
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < rows and 0 <= dy < cols and abs(heights[dx][dy] - heights[x][y]) <= k and (dx, dy) not in visited:
                        visited.add((dx, dy))
                        queue.append((dx, dy))
            
            return False
        
        left, right = 0, 10 ** 6

        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left