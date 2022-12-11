class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        res = []
        pq = [(grid[0][0], 0, 0)]
        grid[0][0] = 0
        orders = []
        currMax = -1

        while pq:
            val, x, y = heappop(pq)
            currMax = max(currMax, val)
            orders.append(currMax)

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != 0:
                    heappush(pq, (grid[dx][dy], dx, dy))
                    grid[dx][dy] = 0
        
        for q in queries:
            res.append(bisect_left(orders, q))
        
        return res