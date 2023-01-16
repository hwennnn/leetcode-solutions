class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        
        for r1, c1, r2, c2 in queries:
            A[r1][c1] += 1
            if c2 + 1 < n:
                A[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                A[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                A[r2 + 1][c2 + 1] += 1
        
        for i in range(n):
            for j in range(1, n):
                A[i][j] += A[i][j - 1]

        for i in range(1, n):
            for j in range(n):
                A[i][j] += A[i - 1][j]

        return A