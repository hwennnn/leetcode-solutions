class Solution:
    def getMaxGridHappiness(self, rows: int, cols: int, introvertsCount: int, extrovertsCount: int) -> int:
        relation = [[0,0,0],[0,-60,-10],[0,-10,40]]
        
        @cache
        def go(index, row, intro, extro):
            if index == -1: return 0
            
            col = index % cols
            res = go(index - 1, (0,) + row[:-1], intro, extro)
            
            if intro > 0:
                score = 120 + relation[1][row[-1]] + (col < cols - 1) * relation[1][row[0]]
                res = max(res, score + go(index - 1, (1,) + row[:-1], intro - 1, extro))
            
            if extro > 0:
                score = 40 + relation[2][row[-1]] + (col < cols - 1) * relation[2][row[0]]
                res = max(res, score + go(index - 1, (2,) + row[:-1], intro, extro - 1))
            
            return res
        
        return go(rows * cols - 1, tuple([0] * cols), introvertsCount, extrovertsCount)