class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[0] * cols for _ in range(rows)]
        rowOnes = defaultdict(int)
        colOnes = defaultdict(int)
        
        for i in range(rows):
            count = grid[i].count(1)
            rowOnes[i] = count
        
        for i, col in enumerate(zip(*grid)):
            count = col.count(1)
            colOnes[i] = count
        
        # print(rowOnes, colOnes)
        for i in range(rows):
            for j in range(cols):
                rone = rowOnes[i]
                rzero = rows - rone
                cone = colOnes[j]
                czero = cols - cone
                # print(i, j, rone, cone, rzero, czero)
                res[i][j] = rone + cone - rzero - czero
        
        return res