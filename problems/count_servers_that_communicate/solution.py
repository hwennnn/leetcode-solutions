class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rc, cc = Counter(), Counter()
        
        for i in range(rows):
            for j,c in enumerate(grid[i]):
                if c == 1:
                    rc[i] += 1
                    cc[j] += 1
        
        res = 0
        for i in range(rows):
            for j,c in enumerate(grid[i]):
                if c == 1 and (rc[i] > 1 or cc[j] > 1):
                    res += 1
        
        return res
        