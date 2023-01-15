class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                A[r][c1] += 1
                if c2 + 1 < n:
                    A[r][c2 + 1] -= 1
        
        res = []
        for i in range(n):
            row = []
            for j in range(n):
                if j == 0:
                    row.append(A[i][j])
                else:
                    row.append(row[-1] + A[i][j])
            
            res.append(row)
        
        return res