class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                mmax = 0
                for di in range(i, i + 3):
                    for dj in range(j, j + 3):
                        mmax = max(mmax, grid[di][dj])
                
                res[i][j] = mmax
        
        return res
        