class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows, cols, a_diag, d_diag = Counter(), Counter(), Counter(), Counter()
        pos = set()
        
        for x, y in lamps:
            if (x, y) not in pos:
                pos.add((x, y))
                rows[x] += 1
                cols[y] += 1
                a_diag[x + y] += 1
                d_diag[x - y] += 1
        
        res = []
        
        for x, y in queries:
            if rows[x] > 0 or cols[y] > 0 or a_diag[x + y] > 0 or d_diag[x - y] > 0:
                res.append(1)
                for dx in range(x - 1, x + 2):
                    for dy in range(y - 1, y + 2):
                        if (dx, dy) in pos:
                            pos.remove((dx, dy))
                            rows[dx] -= 1
                            cols[dy] -= 1
                            a_diag[dx + dy] -= 1
                            d_diag[dx - dy] -= 1
            else:
                res.append(0)
        
        return res
        