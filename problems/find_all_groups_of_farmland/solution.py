class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        res = []
        
        for r1 in range(rows):
            for c1 in range(cols):
                if land[r1][c1] == 0: continue
                
                r2, c2 = r1, c1
                while c2 < cols and land[r2][c2] == 1:
                    c2 += 1
                
                while r2 < rows and land[r2][c1] == 1:
                    r2 += 1
                
                r2 = r2 if r2 == 0 else r2 - 1
                c2 = c2 if c2 == 0 else c2 - 1
                
                res.append([r1, c1, r2, c2])
                
                for row in range(r1, r2 + 1):
                    for col in range(c1, c2 + 1):
                        land[row][col] = 0
        
        return res