class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = set()
        res = 0
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for x, y in stones:
            rows[x].append((x, y))
            cols[y].append((x, y))
        
        def go(x, y):
            visited.add((x, y))
            
            for nx, ny in rows[x] + cols[y]:
                if (nx, ny) not in visited:
                    go(nx, ny)
        
        for x, y in stones:
            if (x, y) not in visited:
                go(x, y)
                res += 1
        
        return n - res