class Solution:
    def latestDayToCross(self, rows: int, cols: int, cells: List[List[int]]) -> int:

        def good(days):
            lands = [[0] * cols for _ in range(rows)]
            
            for i in range(days):
                x, y = cells[i]
                lands[x - 1][y - 1] = 1
            
            queue = collections.deque()
            for y in range(cols):
                if lands[0][y] == 0:
                    queue.append((0, y))
                    lands[0][y] = 1
            
            while queue:
                x, y = queue.popleft()
                if x == rows - 1: return True

                for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= dx < rows and 0 <= dy < cols and lands[dx][dy] == 0:
                        queue.append((dx, dy))
                        lands[dx][dy] = 1
            
            return False
        
        left, right = 1, len(cells)
        res = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return res
            