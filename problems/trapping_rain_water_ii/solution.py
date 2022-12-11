class Solution:
    def trapRainWater(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        res = 0
        visited = [[False] * cols for _ in range(rows)]
        pq = []
        
        for x in range(0, rows):
            visited[x][0] = True
            heappush(pq, (heights[x][0], x, 0))
            visited[x][cols - 1] = True
            heappush(pq, (heights[x][cols - 1], x, cols - 1))
        
        for y in range(cols):
            visited[0][y] = True
            heappush(pq, (heights[0][y], 0, y))
            visited[rows - 1][y] = True
            heappush(pq, (heights[rows - 1][y], rows - 1, y))
        
        while pq:
            h, x, y = heappop(pq)

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and not visited[dx][dy]:
                    visited[dx][dy] = True
                    res += max(0, h - heights[dx][dy])
                    heappush(pq, (max(h, heights[dx][dy]), dx, dy))

        return res