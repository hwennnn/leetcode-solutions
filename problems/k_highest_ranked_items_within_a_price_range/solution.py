class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        heap = []
        sx, sy = start
        minP, maxP = pricing
        queue = deque([(sx, sy, 0)])
        visited = set([(sx, sy)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            price = grid[x][y]

            if price != 1 and minP <= price <= maxP:
                if len(heap) == k:
                    heapq.heappushpop(heap, (-distance, -price, -x, -y))
                else:
                    heapq.heappush(heap, (-distance, -price, -x, -y))

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != 0 and (dx, dy) not in visited:
                    queue.append((dx, dy, distance + 1))
                    visited.add((dx, dy))
        
        return [[-x, -y] for _, _, x, y in sorted(heap, reverse = 1)]
        
        
        