class Solution:
    def highestPeak(self, water: List[List[int]]) -> List[List[int]]:
        rows, cols = len(water), len(water[0])
        res = [[-1] * cols for _ in range(rows)]
        deq = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if water[i][j] == 1:
                    deq.append((i, j))
                    res[i][j] = 0
        
        while deq:
            x, y = deq.popleft()

            for dx,dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and res[dx][dy] == -1:
                    res[dx][dy] = res[x][y] + 1
                    deq.append((dx, dy))
        
        return res